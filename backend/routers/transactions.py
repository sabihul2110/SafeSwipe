# SafeSwipe/backend/routers/transactions.py

from fastapi import APIRouter

from schemas import TransactionRequest, TransactionResponse

router = APIRouter()


@router.post("/transactions/check", response_model=TransactionResponse)
def check_transaction(transaction: TransactionRequest):
    # Placeholder logic only — real ML model will replace this.
    # For now: flag anything over 50000 as suspicious, just to prove the flow works.
    if transaction.amount > 50000:
        return TransactionResponse(
            is_fraud=True,
            reason="Amount unusually high (placeholder rule, not real ML)",
        )
    return TransactionResponse(
        is_fraud=False,
        reason="No issues detected (placeholder rule, not real ML)",
    )