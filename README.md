<img width="729" height="499" alt="Screenshot 2026-11-27 13 37 44" src="https://github.com/user-attachments/assets/921c42ca-ec70-4254-9589-73510ea3c367" />
<img width="729" height="499" alt="Screenshot 2026-11-27 13 39 56" src="https://github.com/user-attachments/assets/36e248de-2e69-4c57-9113-e05baced399f" />
<img width="729" height="499" alt="Screenshot 2026-11-27 13 40 02" src="https://github.com/user-attachments/assets/0114fad1-fa95-4490-b20e-a1f7d89f3231" />
# Customer Message Classifier

A small Python API and web page that classifies incoming customer
messages (order, question, complaint, other) and drafts a reply.
Built for small businesses that want to save time on repetitive
email and chat support.

## Features
- Message classification into 4 categories
- Draft reply generation
- FastAPI backend with interactive docs at `/docs`
- Simple web page for testing at `/`
- Works in **demo mode** without an API key, and uses Claude
  automatically when `ANTHROPIC_API_KEY` is set

## Run locally
```bash
pip install -r requirements.txt
python -m uvicorn app:app --reload
```
Open http://127.0.0.1:8000

## Use real AI replies
Set your key as an environment variable, then restart the server:
```bash
export ANTHROPIC_API_KEY="your-key"
```

## Tech stack
Python, FastAPI, Uvicorn, Anthropic API

## Roadmap
- Email inbox integration (IMAP)
- Custom categories per business
- Reply tone settings
