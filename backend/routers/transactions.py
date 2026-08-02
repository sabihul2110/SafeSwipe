# SafeSwipe/backend/routers/transactions.py

from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas import TransactionRequest, TransactionResponse, TransactionHistoryItem
from core.database import get_db
from models import TransactionRecord

router = APIRouter()


@router.post("/transactions/check", response_model=TransactionResponse)
def check_transaction(transaction: TransactionRequest, db: Session = Depends(get_db)):
    # Placeholder logic only — real ML model will replace this.
    if transaction.amount > 50000:
        is_fraud = True
        reason = "Amount unusually high (placeholder rule, not real ML)"
    else:
        is_fraud = False
        reason = "No issues detected (placeholder rule, not real ML)"

    record = TransactionRecord(
        amount=transaction.amount,
        merchant=transaction.merchant,
        is_fraud=is_fraud,
        reason=reason,
    )
    db.add(record)
    db.commit()

    return TransactionResponse(is_fraud=is_fraud, reason=reason)


@router.get("/transactions", response_model=List[TransactionHistoryItem])
def list_transactions(db: Session = Depends(get_db)):
    records = db.query(TransactionRecord).order_by(TransactionRecord.created_at.desc()).all()
    return records