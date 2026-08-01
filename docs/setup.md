<!-- SafeSwipe/docs/setup.md -->

# SafeSwipe — Setup Guide

## Prerequisites
- Python 3.10+
- Node.js 18+
- npm

## Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn main:app --reload
```
Runs at `http://localhost:8000`.

## Frontend
```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```
Runs at `http://localhost:5173`.

## ML Pipeline
```bash
cd ml
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python train.py
```

## Notes
- Backend and frontend run independently — start both if you need the full app working together.
- `.env` files are git-ignored; always copy from the matching `.env.example`.