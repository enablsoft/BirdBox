# `src/evaluation/confusion_matrix_analysis.py`

Builds species-level confusion matrices from merged detections and labels.

## Usage

```bash
python src/evaluation/confusion_matrix_analysis.py \
  --detections results/Hawaii/merged_detections.csv \
  --labels datasets/Hawaii_testset/annotations.csv \
  --iou-threshold 0.25 \
  --output-path results/Hawaii/confusion_matrix_analysis
```

## Parameters

| Flag | Required | Default | Description |
|---|---|---:|---|
| `--detections` | yes | - | Merged detections CSV (typically from filter-and-merge). |
| `--labels` | yes | - | Ground-truth CSV annotations. |
| `--iou-threshold` | no | `0.5` | Minimum IoU for a valid match. |
| `--use-1d-iou` | no | off | Use time-only IoU (default is 2D time-frequency IoU). |
| `--no-background` | no | off | Exclude background class from matrix. |
| `--single-cls` | no | off | Collapse all classes into one class. |
| `--single-cls-name` | no | `bird` | Name used with single-class mode. |
| `--output-path` | no | `results/confusion_matrix_analysis` | Output directory. |

## Matching Behavior

Confusion-matrix analysis always uses Hungarian optimal matching for deterministic, globally optimal assignment between detections and labels.

Filename normalization removes path/extensions for matching (`recording.wav` and `recording.flac` both normalize to `recording`).

## Output Files

- `confusion_matrix.csv`
- `confusion_matrix_detailed.csv`
- `confusion_matrix_normalized.png`
- `confusion_matrix_raw.png`
- `metadata.txt`

## Files You Interact With

- detections CSV (`--detections`): merged prediction annotations
- labels CSV (`--labels`): reference annotations
- output directory (`--output-path`): matrices, plots, metadata

## Background Class Interpretation

When background is included:

- final **column** (true background) captures false positives
- final **row** (predicted background) captures false negatives

This is useful for separating species-confusion errors from pure detection misses/spurious events.
