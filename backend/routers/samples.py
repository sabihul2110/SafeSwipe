# SafeSwipe/backend/routers/samples.py

from typing import List

from fastapi import APIRouter, HTTPException

from repositories.sample_repository import get_samples, get_sample_by_id
from schemas.sample import SampleSummary, SamplePredictionResponse
from services.ml_service import predict_from_features

router = APIRouter()


@router.get("/samples", response_model=List[SampleSummary])
def list_samples():
    df = get_samples()
    return [
        SampleSummary(sample_id=int(row.sample_id), amount=float(row.Amount), actual_label=int(row.Class))
        for _, row in df.iterrows()
    ]


@router.post("/samples/{sample_id}/predict", response_model=SamplePredictionResponse)
def predict_sample(sample_id: int):
    row = get_sample_by_id(sample_id)
    if row is None:
        raise HTTPException(status_code=404, detail="Sample not found")

    features = row.drop(labels=["sample_id", "Class"]).to_frame().T
    predicted_fraud, probability = predict_from_features(features)

    return SamplePredictionResponse(
        sample_id=int(row.sample_id),
        amount=float(row.Amount),
        actual_label=int(row.Class),
        predicted_fraud=predicted_fraud,
        fraud_probability=probability,
    )