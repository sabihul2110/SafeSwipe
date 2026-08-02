# SafeSwipe/backend/services/transaction_service.py

from sqlalchemy.orm import Session

from repositories.transaction_repository import create_transaction, get_all_transactions


def evaluate_and_save_transaction(db: Session, amount: float, merchant: str):
    # Placeholder logic only — real ML model will replace this.
    if amount > 50000:
        is_fraud = True
        reason = "Amount unusually high (placeholder rule, not real ML)"
    else:
        is_fraud = False
        reason = "No issues detected (placeholder rule, not real ML)"

    create_transaction(db, amount, merchant, is_fraud, reason)
    return is_fraud, reason


def list_transaction_history(db: Session):
    return get_all_transactions(db)