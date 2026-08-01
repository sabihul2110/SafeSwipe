# SafeSwipe/backend/schemas.py

from pydantic import BaseModel


class TransactionRequest(BaseModel):
    amount: float
    merchant: str


class TransactionResponse(BaseModel):
    is_fraud: bool
    reason: str