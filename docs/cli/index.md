# CLI Reference

This section documents all user-facing parameters for the core executable modules.

## Covered Commands

- `src/inference/detect_birds.py`
- `src/evaluation/f_beta_score_analysis.py`
- `src/evaluation/filter_and_merge_detections.py`
- `src/evaluation/confusion_matrix_analysis.py`
- `src/streamlit/app.py` (launch command + interactive controls)

## Evaluation Order

For robust evaluation, use this order:

1. `detect_birds.py --no-merge`
2. `f_beta_score_analysis.py`
3. `filter_and_merge_detections.py`
4. `confusion_matrix_analysis.py`

## Notes on Defaults

Defaults are taken from the current source files in `src/`. If examples elsewhere differ, prefer this reference and verify with `--help`.
