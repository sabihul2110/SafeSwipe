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


def predict_from_features(features_df):
    model = _load_model()
    prediction = model.predict(features_df)[0]
    probability = model.predict_proba(features_df)[0][1]
    return bool(prediction), float(probability)