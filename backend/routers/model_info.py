# SafeSwipe/backend/routers/model_info.py

from fastapi import APIRouter

from schemas.model_info import ModelInfo
from services.ml_service import FRAUD_THRESHOLD

router = APIRouter()

# These metrics come from ml/tune_threshold.py's real evaluation run at the
# chosen threshold — see docs/model_card.md for the full comparison table.
MODEL_PRECISION = 0.88
MODEL_RECALL = 0.83
MODEL_F1 = 0.85


@router.get("/model-info", response_model=ModelInfo)
def get_model_info():
    return ModelInfo(
        model_name="Random Forest (100 trees, class-weighted)",
        threshold=FRAUD_THRESHOLD,
        precision=MODEL_PRECISION,
        recall=MODEL_RECALL,
        f1_score=MODEL_F1,
        threshold_reasoning=(
            "Threshold set to 0.4 instead of the default 0.5 because missing "
            "real fraud is generally costlier than a false alarm — this "
            "trades a small amount of precision for meaningfully higher recall."
        ),
    )
