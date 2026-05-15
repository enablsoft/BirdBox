"""
BirdBox dependency bootstrap script.

This script exists to resolve PyTorch installation mode automatically:
CPU/MPS on macOS or non-NVIDIA systems, and CUDA (cu118) on NVIDIA systems.
Without that torch-mode resolution, setup would usually be just:
pip install -r requirements.txt
"""

import platform
import subprocess
import sys
import argparse

PYTHON_VERSION = (3, 12)
TORCH_VERSION = "2.5.1"
TORCHVISION_VERSION = "0.20.1"
PYTORCH_CPU_INDEX_URL = "https://download.pytorch.org/whl/cpu"
PYTORCH_CUDA_INDEX_URL = "https://download.pytorch.org/whl/cu118"


# -----------------------------
# Helpers
# -----------------------------

def run(cmd):
    print(f"\n>>> {' '.join(cmd)}\n")
    subprocess.check_call(cmd)


def pip_install(*args):
    run([sys.executable, "-m", "pip", "install", *args])


def has_nvidia_gpu():
    """
    Detect NVIDIA GPU via nvidia-smi.
    Works on most Linux/Windows systems with drivers installed.
    """
    try:
        result = subprocess.run(
            ["nvidia-smi"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False


def is_macos():
    return platform.system() == "Darwin"


def require_python_312():
    if sys.version_info[:2] != PYTHON_VERSION:
        expected = f"{PYTHON_VERSION[0]}.{PYTHON_VERSION[1]}"
        current = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        raise SystemExit(
            f"Unsupported Python version: {current}. "
            f"This project requires Python {expected}.x."
        )


# -----------------------------
# PyTorch installer logic
# -----------------------------

def install_torch(mode):
    """
    mode: cpu | cuda | auto
    """

    if mode == "cpu":
        print("Forcing CPU PyTorch install (matching environment-cpu.yml)")
        pip_install(
            f"torch=={TORCH_VERSION}",
            f"torchvision=={TORCHVISION_VERSION}",
            "--index-url",
            PYTORCH_CPU_INDEX_URL
        )
        return

    if mode == "cuda":
        print("Forcing CUDA PyTorch install (cu118, matching environment-gpu.yml)")
        pip_install(
            f"torch=={TORCH_VERSION}",
            f"torchvision=={TORCHVISION_VERSION}",
            "--index-url",
            PYTORCH_CUDA_INDEX_URL
        )
        return

    # AUTO mode
    if is_macos():
        print("Detected macOS -> installing CPU/MPS PyTorch")
        pip_install(
            f"torch=={TORCH_VERSION}",
            f"torchvision=={TORCHVISION_VERSION}"
        )
        return

    if has_nvidia_gpu():
        print("Detected NVIDIA GPU -> installing CUDA PyTorch (cu118)")
        pip_install(
            f"torch=={TORCH_VERSION}",
            f"torchvision=={TORCHVISION_VERSION}",
            "--index-url",
            PYTORCH_CUDA_INDEX_URL
        )
        return

    print("No GPU detected -> installing CPU PyTorch")
    pip_install(
        f"torch=={TORCH_VERSION}",
        f"torchvision=={TORCHVISION_VERSION}",
        "--index-url",
        PYTORCH_CPU_INDEX_URL
    )


# -----------------------------
# Main dependency install
# -----------------------------

def install_requirements():
    print("Installing project dependencies from requirements.txt")
    pip_install("-r", "requirements.txt")


# -----------------------------
# Environment check
# -----------------------------

def print_env_info():
    print("\n==============================")
    print("BirdBox installation starting")
    print("==============================")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Python: {sys.version}")
    print("==============================\n")


# -----------------------------
# Main
# -----------------------------

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--mode",
        choices=["auto", "cpu", "cuda"],
        default="auto",
        help="Installation mode (default: auto)"
    )

    args = parser.parse_args()

    print_env_info()
    require_python_312()

    # Upgrade pip first (important for PyTorch wheels)
    pip_install("--upgrade", "pip")

    # Install PyTorch first (critical dependency order)
    install_torch(args.mode)

    # Install the rest of your stack
    install_requirements()

    print("\n===================================")
    print("BirdBox installation complete ✔")
    print("===================================\n")


if __name__ == "__main__":
    main()