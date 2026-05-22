# Troubleshooting Notes

## No Detections

- Verify model/mapping pair (`--model` and `--species-mapping`) are compatible.
- Lower confidence (`--conf`) for exploratory runs (`0.1` or lower, often `0.001` for raw capture).
- Check audio format and quality; WAV/FLAC outperform lossy MP3/OGG for faint calls.
- Confirm audio file actually contains event times covered by labels (evaluation runs).

## Too Many False Positives

- Increase `--conf` first.
- Reduce `--song-gap` to prevent over-aggregation of unrelated events.
- Tune `--nms-iou` for duplicate suppression behavior.
- Validate with confusion matrix background row/column to separate species confusion vs generic noise hits.

## Memory or Runtime Issues

- Reduce parallelism (`--workers`, `--num-workers`).
- Process subsets of files and merge reports afterward.
- Prefer GPU-backed runs for large jobs when available.
- Keep raw detections once; avoid re-running inference during threshold experiments.

## Filename Mismatch in Evaluation

Evaluation matches filenames by normalized stem:

- `recording_01.wav` and `recording_01.flac` match
- `siteA_recording_01.wav` and `recording_01.flac` do not match

If matching fails, inspect both CSV/JSON filename fields and unify base names before rerunning metrics.
