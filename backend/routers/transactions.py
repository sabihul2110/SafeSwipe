# SafeSwipe/backend/routers/transactions.py

from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.transaction import TransactionRequest, TransactionResponse, TransactionHistoryItem
from core.database import get_db
from services.transaction_service import (
    evaluate_and_save_transaction,
    list_transaction_history,
    clear_transaction_history,
)

router = APIRouter()


@router.post("/transactions/check", response_model=TransactionResponse)
def check_transaction(transaction: TransactionRequest, db: Session = Depends(get_db)):
    is_fraud, reason = evaluate_and_save_transaction(db, transaction.amount, transaction.merchant)
    return TransactionResponse(is_fraud=is_fraud, reason=reason)


@router.get("/transactions", response_model=List[TransactionHistoryItem])
def list_transactions(db: Session = Depends(get_db)):
    return list_transaction_history(db)


@router.delete("/transactions")
def clear_transactions(db: Session = Depends(get_db)):
    clear_transaction_history(db)
    return {"status": "cleared"}