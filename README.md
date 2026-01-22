# AI-Powered-Image-Captioning-System

Minimal setup:

1) Create a virtualenv and install deps:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2) Run the server from the repo root:
```bash
uvicorn backend.main:app --reload
```

3) Open `http://127.0.0.1:8000`
