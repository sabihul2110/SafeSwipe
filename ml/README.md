<!-- SafeSwipe/ml/README.md -->

# SafeSwipe ML Pipeline

This folder holds the data pipeline and model training work — everything related to turning the Kaggle dataset into a working fraud-detection model.

## Status
Scaffolding only — no notebooks or scripts written yet.

## Stack
- Python 3
- pandas, scikit-learn (to start)

## Dataset
This project uses the Kaggle "Credit Card Fraud Detection" dataset. It's not included in the repo (too large, and shouldn't live in Git). To get it:
1. Download `creditcard.csv` from Kaggle.
2. Place it at `ml/data/creditcard.csv`.

## Setup (placeholder)
```bash
cd ml
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```