# SIGNAL/NOISE — Cybersecurity Portfolio

Source for my cybersecurity portfolio, live at **[zdemanche.github.io/Website](https://zdemanche.github.io/Website/)**.

## Design

A "case-file dossier" theme: cool paper and ink palette with a single alert-amber accent, set in IBM Plex (Sans Condensed / Sans / Mono). Projects are presented as numbered files with monospace metadata rows.

## Stack

- Hand-written HTML5 + CSS3 — no frameworks, no build step
- Only external dependency: Google Fonts (IBM Plex)
- `prefers-reduced-motion` respected; keyboard focus states; responsive to mobile

## Contents

| Path | What it is |
|------|------------|
| `index.html` / `styles.css` | The portfolio page |
| `chatbot-demo.html` / `chatbot-code.html` | UConn Chatbot demo and code walkthrough |
| `Projects.py/` | Python security tools + PDF documentation |
| `assets/resume.pdf` | Resume |

## Local development

```bash
git clone https://github.com/zdemanche/Website.git
cd Website
python3 -m http.server 8000
# visit http://localhost:8000
```

## Deployment

Deployed automatically via GitHub Pages on every push to `main`.

© 2026 Zachary Demanche. All rights reserved.
