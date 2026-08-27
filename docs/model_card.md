<!-- SafeSwipe/docs/model_card.md -->

# SafeSwipe — Model Card

## Model
Random Forest Classifier (scikit-learn), `class_weight="balanced"`, 100 trees, trained on unscaled features.

## Why Random Forest
We first tried Logistic Regression as a baseline. It caught fraud well (92% recall) but produced far too many false alarms (6% precision — only 1 in ~17 flagged transactions was actually fraud). Random Forest was tried as a comparison and performed substantially better overall. See "Model Comparison" below.

## Training Data
Kaggle "Credit Card Fraud Detection" dataset — 284,807 transactions, 31 features (Time, Amount, V1–V28 anonymized PCA components), severely imbalanced (99.83% legitimate, 0.17% fraud). 80/20 stratified train/test split.

## Model Comparison (test set, fraud class)
| Metric | Logistic Regression | Random Forest (chosen) |
|---|---|---|
| Precision | 0.06 | 0.92 |
| Recall | 0.92 | 0.79 |
| F1-score | 0.11 | 0.85 |

## What this means in practice
Random Forest catches 79% of actual fraud cases, and when it does flag a transaction as fraud, it's right 92% of the time — a much more usable balance than the Logistic Regression baseline, which drowned real fraud alerts in false positives.

## Limitations
- Recall is lower than the Logistic Regression baseline (79% vs 92%) — roughly 1 in 5 fraud cases is missed. This is a real tradeoff, not solved, just chosen deliberately for fewer false alarms.
- Trained on anonymized, PCA-transformed features — limited real-world interpretability of individual predictions.
- Trained on one static, historical dataset — not validated against real-time or newer fraud patterns.
- Classification threshold is the default (0.5) — not yet tuned for a specific business cost tradeoff between missed fraud and false alarms.

## Threshold Tuning
Tested thresholds from 0.3 to 0.8 (see `ml/tune_threshold.py`). Final choice: **0.4** (instead of the default 0.5) — improves recall to 83% (catching more real fraud) while keeping precision at 88%, since missing fraud is generally costlier than a false alarm.

| Threshold | Precision | Recall | F1 |
|---|---|---|---|
| 0.3 | 0.83 | 0.85 | 0.84 |
| 0.4 (chosen) | 0.88 | 0.83 | 0.85 |
| 0.5 (default) | 0.91 | 0.79 | 0.84 |
| 0.6 | 0.95 | 0.78 | 0.85 |
| 0.7 | 0.97 | 0.76 | 0.85 |
| 0.8 | 0.97 | 0.68 | 0.80 |

## Not yet done
- Cross-validation (currently a single train/test split)
- Testing on more recent or synthetic fraud patterns beyond this dataset