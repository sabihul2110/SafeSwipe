# SafeSwipe/backend/schemas/sample.py

from pydantic import BaseModel


class SampleSummary(BaseModel):
    sample_id: int
    amount: float
    actual_label: int  # 0 = legit, 1 = fraud, from the real dataset


class SamplePredictionResponse(BaseModel):
    sample_id: int
    amount: float
    actual_label: int
    predicted_fraud: bool
    fraud_probability: float