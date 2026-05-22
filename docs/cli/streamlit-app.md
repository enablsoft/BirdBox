# `src/streamlit/app.py`

Streamlit web interface for interactive detection, visualization, and export.

## Launch

```bash
streamlit run src/streamlit/app.py
```

## Runtime Behavior

- discovers models under `models/` (`.pt`, `.onnx`, `.engine`)
- auto-selects species mapping using `config.get_species_mapping_for_model(...)`
- creates a per-session `BirdCallDetector`
- uses the same inference primitives as CLI (`detect_single_file`)

## Sidebar Controls

| Control | Default | Range / Options | Effect |
|---|---:|---|---|
| Model selector | first model found | models in `models/` | Chooses detector model and species mapping. |
| Download Default Model | - | button | Attempts model download from configured URL. |
| Confidence Threshold | `0.18` | `0.01` to `0.8` | Passed to detector as confidence threshold. |
| Song Gap Threshold (seconds) | `0.1` | `0.0` to `2.0` | Merge gap for reconstructing song segments. |

Fixed in app code:

- NMS IoU = `0.5`
- concurrency control enabled
- `MAX_CONCURRENT_DETECTIONS` from `src/config.py`

## User-Provided File Inputs

- uploader supports: WAV, FLAC, OGG, MP3
- files longer than `MAX_DURATION_SECONDS` (`600`) are truncated to first 10 minutes
- lossy format warning shown for MP3/OGG

## Produced Artifacts (Download Buttons)

- JSON with algorithm metadata
- simplified CSV
- Xeno-Canto Annota-JSON
- Raven selection table (`.txt`)

## Files You Interact With

- uploaded audio file in browser session
- model files in `models/`
- species mapping definitions in `src/config.py` (indirect through auto mapping)
- optional logo asset `docs/img/logo_birdbox.png`
- optional downloaded temporary model archive/content when using "Download Default Model"

## Visual Layer

- builds full-duration PCEN spectrogram render
- overlays detection boxes and species labels
- uses species-specific colors from mapping config
- caches spectrogram image by audio + detections signature
