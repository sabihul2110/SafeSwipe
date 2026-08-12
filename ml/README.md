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

## Setup
```bash
cd ml
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python train.py
```

Running `train.py` prints evaluation metrics (precision, recall, F1) and saves two files to `model/`:
- `fraud_model.joblib` — the trained logistic regression model
- `scaler.joblib` — the feature scaler, required to correctly scale any new transaction the same way training data was scaled

## Current model
Random Forest (`class_weight="balanced"`, 100 trees), trained on unscaled features (tree-based models don't require scaling). Chosen after comparing against Logistic Regression — see `docs/model_card.md` for full metrics. Result: ~79% recall, ~92% precision — far fewer false alarms than the Logistic Regression baseline, at a modest recall cost.

`compare_models.py` holds the original comparison between both models, kept for reference.