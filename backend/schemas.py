# SafeSwipe/backend/schemas.py

from pydantic import BaseModel


class TransactionRequest(BaseModel):
    amount: float
    merchant: str


class TransactionResponse(BaseModel):
    is_fraud: bool
    reason: str


class TransactionHistoryItem(BaseModel):
    id: int
    amount: float
    merchant: str
    is_fraud: bool
    reason: str

    class Config:
        from_attributes = True