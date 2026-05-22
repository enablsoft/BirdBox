# `src/evaluation/f_beta_score_analysis.py`

Confidence-threshold sweep and F-beta evaluation against ground-truth labels.

## Purpose

For each confidence threshold:

1. filter raw detections (`confidence >= threshold`)
2. merge temporally adjacent detections (`reconstruct_songs`)
3. match detections to labels with IoU
4. compute precision/recall/F-beta (per class + aggregate)

## Usage

```bash
python src/evaluation/f_beta_score_analysis.py \
  --detections results/Hawaii/raw_detections.json \
  --labels datasets/Hawaii_testset/annotations.csv \
  --conf-range 0.00 1.0 0.01 \
  --beta 1.0 \
  --iou-threshold 0.25 \
  --song-gap 0.1 \
  --num-workers 8 \
  --output-path results/Hawaii/f_1.0_score_analysis
```

## Parameters

| Flag | Required | Default | Description |
|---|---|---:|---|
| `--detections` | yes | - | Raw detections JSON from `detect_birds.py --no-merge`. |
| `--labels` | yes | - | Ground-truth CSV (`Filename`, time/frequency, species columns). |
| `--conf-range MIN MAX STEP` | no | `0.00 1.0 0.01` | Threshold grid for sweep. |
| `--beta` | no | `1.0` | F-beta weighting (`>1` favors recall, `<1` favors precision). |
| `--iou-threshold` | no | `0.5` | Match threshold for IoU. |
| `--song-gap` | no | JSON config or `0.1` | Merge gap override in seconds. |
| `--single-cls` | no | off | Collapse all species into one class. |
| `--single-cls-name` | no | `bird` | Label used with `--single-cls`. |
| `--no-optimal-matching` | no | off | Use greedy matching instead of Hungarian optimal matching. |
| `--no-plot` | no | off | Skip PNG plot generation. |
| `--output-path` | no | `results/f_beta_score_analysis` | Result directory. |
| `--num-workers` | no | `1` | Process count for threshold-parallel analysis. |

## Matching Modes

- default: Hungarian optimal matching (order-independent)
- optional: greedy matching (order-dependent, faster in some scenarios)

## Generated Artifacts

- `f{beta}_score_analysis.csv`
- `f{beta}_score_analysis.json`
- `optimal_thresholds.csv`
- performance plots (`overall_micro`, `overall_macro`, `micro_vs_macro`, per-class curves, heatmap)

## Files You Interact With

- detections input JSON (`--detections`): raw detections from inference
- labels input CSV (`--labels`): ground-truth annotations
- output directory (`--output-path`): tables and plots for downstream selection/reporting

## Interpretation

- **micro average**: sums TP/FP/FN over all classes (frequency-weighted)
- **macro average**: arithmetic mean across classes (class-balanced)

Use macro trends to detect minority-class collapse, even if micro score looks strong.
