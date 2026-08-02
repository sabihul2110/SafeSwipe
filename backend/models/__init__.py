# SafeSwipe/backend/models/__init__.py

from core.database import Base
from models.transaction import TransactionRecord

__all__ = ["Base", "TransactionRecord"]