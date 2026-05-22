# `src/inference/detect_birds.py`

Main inference entrypoint for single files or directory batches.

## Usage

```bash
python src/inference/detect_birds.py \
  --audio datasets/Hawaii_testset/soundscape_data \
  --model models/Hawaii.pt \
  --species-mapping Hawaii \
  --output-path results/Hawaii/raw_detections \
  --output-format json-with-algorithm-metadata \
  --conf 0.001 \
  --no-merge
```

## Parameters

| Flag | Required | Default | Description |
|---|---|---:|---|
| `--audio` | yes | - | Input path: audio file or directory. Supported extensions: WAV/FLAC/OGG/MP3. |
| `--model` | yes | - | YOLO model path (`.pt`, `.onnx`, `.engine`, ...). |
| `--species-mapping` | yes | - | Mapping key used to decode class ids to species names. |
| `--output-path` | no | `results/all_detections` | Base output path (extension added per format). |
| `--output-format` | no | `json-with-algorithm-metadata` | One of `json-with-algorithm-metadata`, `simplified-csv`, `xeno-canto-annota-json`, `raven-selection-table`, `all`. |
| `--conf` | no | `0.2` | YOLO confidence threshold. |
| `--nms-iou` | no | `0.7` | IoU threshold used by YOLO/NMS stages. |
| `--song-gap` | no | `0.1` | Max temporal gap (seconds) for merging neighboring detections into one song segment. |
| `--workers` | no | `1` | Parallel workers. Each worker loads its own model copy. |
| `--no-merge` | no | off | Keep raw detections (recommended for threshold sweeps). |

### Allowed `--species-mapping` values

- `Just-Bird`
- `All-In-One`
- `Hawaii`
- `Northeastern-US`
- `Southern-Sierra-Nevada`
- `Western-US`
- `Amazon-Basin`

## Output Files

The base `--output-path` is expanded depending on format:

- `json-with-algorithm-metadata` -> `*.json`
- `simplified-csv` -> `*.csv`
- `xeno-canto-annota-json` -> `*.xc.json`
- `raven-selection-table` -> `*.txt` (single-file) or `*_raven/` directory (multi-file)
- `all` -> all of the above

## Files You Interact With

- input audio: path passed via `--audio` (single file or directory tree)
- model artifact: file passed via `--model`
- mapping selection: logical dataset key via `--species-mapping`
- output artifact base: path passed via `--output-path`
- taxonomy mapping used for Xeno-Canto export: `taxonomies/Cornell-to-AviList-mapping.json` (indirectly via exporter)

## JSON Structure (Core Fields)

- top-level: `audio_file`/`audio_files`, `model_config`, `detection_count`, `detections`
- detection-level:
  - species: `species`, `species_id`
  - confidence: `confidence` (raw) or `avg_confidence`/`max_confidence` (merged)
  - geometry: `time_start`, `time_end`, `freq_low_hz`, `freq_high_hz`
  - multi-file metadata: `filename`, `file_path`

## Operational Recommendations

- For evaluation, run with:
  - low `--conf` (e.g. `0.001`)
  - `--no-merge`
  - JSON output
- Then optimize threshold in `f_beta_score_analysis.py` and apply exactly once with `filter_and_merge_detections.py`.
