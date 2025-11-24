Resume preview & PDF generator

This repo now includes a print-friendly resume page and a Node-based PDF generator.

How to preview locally

1. Start a local HTTP server from the project root (Python built-in):

```bash
cd /path/to/ashutoshcp.github.io
python3 -m http.server 8000
```

2. Open the site in your browser:

```bash
open http://localhost:8000
# or direct resume view
open http://localhost:8000/resume.html
```

Generate a printable PDF using Puppeteer

1. Install dev dependencies (you need Node.js + npm):

```bash
npm install
```

2. Start the local server (see above) and then run:

```bash
npm run resume:pdf
```

This will launch a headless browser, load the print-friendly `resume.html`, and write `docs/resume-print.pdf`.

Notes
- If Puppeteer fails due to missing Chrome binary on your system, install the full puppeteer package (already in devDependencies) and ensure a compatible Chromium is available. On CI, consider using `puppeteer-core` plus a system-provided Chrome.
- The `resume.html` is intentionally print-friendly and contains a `window.print()` button for manual PDF generation.

Accessibility & TOC
- A floating Table of Contents is generated on pages containing the `#resume` section to help navigation. It's hidden when printing.

