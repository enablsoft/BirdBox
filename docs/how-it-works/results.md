# Results

By default, BirdBox writes outputs under `results/`.

## Recommended Layout

```text
results/
  <dataset_name>/
    raw_detections.json
    f_1.0_score_analysis/
      f1.0_score_analysis.csv
      optimal_thresholds.csv
      ...
    merged_detections.json
    merged_detections.csv
    confusion_matrix_analysis/
      confusion_matrix.csv
      confusion_matrix_normalized.png
      metadata.txt
```

## Reproducibility Tips

- keep one subfolder per dataset/model configuration
- preserve raw detections JSON (it is the source for threshold experiments)
- archive the exact threshold and song-gap used for final exports
