# Models

BirdBox accepts YOLO model artifacts in multiple formats (`.pt`, `.onnx`, `.engine`).

## Shipped Naming Convention

Model file names typically encode mapping identity:

- `All-In-One.pt`
- `Amazon-Basin.pt`
- `Hawaii.pt`
- `Just-Bird.pt`
- `Northeastern-US.pt`
- `Southern-Sierra-Nevada.pt`
- `Western-US.pt`

## Mapping Compatibility

The class-id decoding depends on the selected mapping:

- CLI: pass explicit `--species-mapping`
- Streamlit: mapping is inferred from model file name using `config.get_species_mapping_for_model(...)`

If model and mapping disagree, species labels in output are invalid.

## Best Practice

Keep the following tuple together in experiment records:

- model file path
- mapping name
- confidence threshold
- song-gap
- NMS IoU


# Datasets

BirdBox evaluation examples assume dataset folders under `datasets/`.

## Typical Structure

```text
datasets/
  <dataset_name>/
    soundscape_data/
      *.wav|*.flac|*.ogg|*.mp3
    annotations.csv
```

## Required Files for Evaluation

- `soundscape_data/` for inference input
- `annotations.csv` for F-beta and confusion-matrix analyses

## Naming Consistency

Annotation filenames and detection filenames are matched by base name.

Example:

- detection: `site_001.wav`
- label: `site_001.flac`

These still match because extension is normalized out.
