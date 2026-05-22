<div align="center">
  <h1>BirdBox</h1>
  <img src="img/logo_birdbox.png" width="250" alt="BirdBox-Logo" />
  
  
  <p><strong>Deep Learning Bird Call Detection & Evaluation System</strong></p>
  
  <a href="https://github.com/birdnet-team/BirdBox/blob/main/LICENSE" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/license-MIT-brightgreen.svg" alt="License"></a>
  <a href="https://www.python.org/downloads/release/python-3120/" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/python-3.12-blue.svg" alt="Python 3.12"></a>
  <img src="https://img.shields.io/badge/species-282-brightgreen" alt="Species 282">

</div>

BirdBox is a comprehensive system for detecting and evaluating bird calls in audio recordings using deep learning. It leverages YOLO (You Only Look Once) object detection on spectrogram images to identify and localize bird vocalizations in time and frequency.

# BirdBox

BirdBox is a technical detection and evaluation stack for avian bioacoustics:

- inference on arbitrary-length recordings with YOLO models on PCEN spectrogram clips
- species-aware post-processing that reconstructs continuous song segments
- evaluation tooling for threshold optimization and confusion-matrix diagnostics
- a Streamlit frontend that reuses the core inference implementation

## Scope

BirdBox focuses on **acoustic event detection and evaluation**, not model training.
Training-time preprocessing and dataset preparation live in companion repositories (for example BirdBox-Train), while this repository provides inference, post-processing, and evaluation for trained models.

## End-to-End Workflow

```mermaid
flowchart LR
    A["Audio input<br/>WAV/FLAC/OGG/MP3"] --> B["detect_birds.py<br/>raw detections (--no-merge)"]
    B --> C["f_beta_score_analysis.py<br/>threshold sweep + metrics"]
    C --> D["filter_and_merge_detections.py<br/>apply chosen threshold"]
    D --> E["confusion_matrix_analysis.py<br/>species-level diagnostics"]
```

## Interfaces

- **CLI**: full pipeline control, batch processing, reproducible outputs.
- **Web app**: `streamlit run src/streamlit/app.py` for interactive inspection and export.

## Quick Links

- Installation and environment setup: `getting-started/installation.md`
- Minimal run commands: `getting-started/quickstart.md`
- Signal-processing and detection internals: `pipeline/detect-birds-internals.md`
- Complete CLI parameter reference: `cli/index.md`
- Input/output schemas and artifact definitions: `formats/index.md`

