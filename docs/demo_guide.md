# SafeSwipe — Demo Guide

How to run the full app locally for a live demo or review.

## 1. Start the backend
```bash
cd backend
source venv/bin/activate
uvicorn main:app --reload
```
Runs at http://localhost:8000. Confirm it's up by visiting http://localhost:8000/health.

## 2. Start the frontend
In a new terminal tab:
```bash
cd frontend
npm run dev
```
Runs at http://localhost:5173.

## 3. What to show
- Real ML Model Demo: click "Check" on any sample transaction — shows the trained Random Forest model's live prediction vs. the actual real-world outcome.
- Simple Rule-Based Demo: a basic form, clearly separate from the real model.

## If something looks broken
- Blank sample list / no predictions -> backend isn't running. Check the backend terminal for errors.
- Errors in the browser -> confirm backend is on port 8000 and frontend is pointed at http://localhost:8000.
