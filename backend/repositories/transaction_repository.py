# SafeSwipe/backend/repositories/transaction_repository.py

from sqlalchemy.orm import Session

from models import TransactionRecord


def create_transaction(db: Session, amount: float, merchant: str, is_fraud: bool, reason: str) -> TransactionRecord:
    record = TransactionRecord(amount=amount, merchant=merchant, is_fraud=is_fraud, reason=reason)
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def get_all_transactions(db: Session):
    return db.query(TransactionRecord).order_by(TransactionRecord.created_at.desc()).all()



def delete_all_transactions(db: Session):
    db.query(TransactionRecord).delete()
    db.commit()