# SafeSwipe/backend/services/ml_service.py

import os

import joblib

MODEL_PATH = os.path.join("..", "ml", "model", "fraud_model.joblib")

_model = None


def _load_model():
    global _model
    if _model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model not found at {MODEL_PATH}. Run ml/train.py first.")
        _model = joblib.load(MODEL_PATH)
    return _model


# Tuned via ml/tune_threshold.py — 0.4 gives better recall (catches more
# fraud) than the default 0.5, at only a small precision cost. In fraud
# detection, missing real fraud is generally costlier than a false alarm.
FRAUD_THRESHOLD = 0.4


def predict_from_features(features_df):
    model = _load_model()
    probability = model.predict_proba(features_df)[0][1]
    prediction = probability >= FRAUD_THRESHOLD
    return bool(prediction), float(probability)