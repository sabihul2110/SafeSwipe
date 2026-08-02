# SafeSwipe/backend/services/ml_service.py

import os

import joblib

MODEL_PATH = os.path.join("..", "ml", "model", "fraud_model.joblib")
SCALER_PATH = os.path.join("..", "ml", "model", "scaler.joblib")

_model = None
_scaler = None


def _load_artifacts():
    global _model, _scaler
    if _model is None or _scaler is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model not found at {MODEL_PATH}. Run ml/train.py first.")
        _model = joblib.load(MODEL_PATH)
        _scaler = joblib.load(SCALER_PATH)
    return _model, _scaler


def predict_from_features(features_df):
    model, scaler = _load_artifacts()
    scaled = scaler.transform(features_df)
    prediction = model.predict(scaled)[0]
    probability = model.predict_proba(scaled)[0][1]
    return bool(prediction), float(probability)