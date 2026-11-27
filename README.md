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