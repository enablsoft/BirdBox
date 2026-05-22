# Inputs and Labels

## Audio Inputs

`detect_birds.py` accepts:

- single audio file path
- or a directory (searched recursively)

Supported extensions:

- `.wav`
- `.flac`
- `.ogg`
- `.mp3`

Notes:

- lossy formats are supported but can reduce recall for faint/high-frequency calls
- stereo content is collapsed to mono

## Model Files

Supported model artifacts are passed to `--model`:

- `.pt`
- `.onnx`
- `.engine`
- other YOLO-compatible formats

The selected species mapping must match the model training label space.

## Species Mapping Source

Mappings are loaded from `src/config.py` via:

- `get_species_mapping_for_model(model_path)` (app-side model-name inference)
- `get_species_mapping(species_mapping_name)` (explicit mapping retrieval)

The mapping object provides:

- class id -> eBird code
- eBird code -> display name
- class id -> color
- fixed clip/image defaults used in inference

## Ground-Truth Labels CSV

Evaluation scripts expect a CSV with these columns:

```text
Filename,Start Time (s),End Time (s),Low Freq (Hz),High Freq (Hz),Species eBird Code
```

Conventions:

- time in seconds
- frequencies in Hz
- species as eBird code
- filename matching is normalized by base name (extension removed)
