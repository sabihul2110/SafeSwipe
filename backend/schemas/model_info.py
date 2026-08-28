# SafeSwipe/backend/schemas/model_info.py

from pydantic import BaseModel


class ModelInfo(BaseModel):
    model_name: str
    threshold: float
    precision: float
    recall: float
    f1_score: float
    threshold_reasoning: str
