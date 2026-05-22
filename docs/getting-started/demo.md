# Demo



## Streamlit Interface

![Streamlit UI](../img/streamlit_ui_screenshot.png)


Yes, this is possible, with one important caveat:
Material for MkDocs can render the page and embed web content, but it cannot execute the Python/Streamlit inference pipeline on its own.

To get the same behavior as `src/streamlit/app.py` (file upload, model selection, and spectrogram with bounding boxes), the recommended approach is to host the Streamlit app and embed it here.

## Recommended Architecture

- **UI shell**: Material for MkDocs page (`docs/demo/overview.md`)
- **Interactive runtime**: hosted Streamlit app (same code as `src/streamlit/app.py`)
- **Embed method**: `iframe`

This keeps the docs static and fast, while the demo remains fully interactive.

## Embedded Demo

Replace `https://YOUR-STREAMLIT-URL` with your deployed Streamlit URL.

<iframe
  src="https://YOUR-STREAMLIT-URL"
  width="100%"
  height="900"
  style="border: 1px solid var(--md-default-fg-color--lightest); border-radius: 8px;"
  loading="lazy"
  title="BirdBox interactive demo"
></iframe>

## Local Alternative

If you do not want to host the demo yet, users can run the same interface locally:

```bash
streamlit run src/streamlit/app.py
```

That local app already includes:

- audio file upload (`wav`, `flac`, `ogg`, `mp3`)
- model selection from `models/`
- PCEN spectrogram generation
- detection bounding boxes and labels

## Notes

- GitHub Pages/MkDocs hosting is static, so model inference must run in a separate service (like Streamlit Cloud, Hugging Face Spaces, or your own server).
- If embedding is blocked by browser security headers, link out to the hosted demo page instead of using an iframe.