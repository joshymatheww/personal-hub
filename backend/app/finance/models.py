from datetime import UTC, datetime
from enum import Enum

from sqlalchemy import DateTime, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class AccountType(str, Enum):
    BANK_ACCOUNT = "bank_account"
    CREDIT_CARD = "credit_card"
    POCKET_WALLET = "pocket_wallet"


class PaymentMode(str, Enum):
    CASH = "cash"
    UPI = "upi"
    NET_BANKING = "net_banking"
    CREDIT_CARD_DIRECT = "credit_card_direct"


class TransactionType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"
    TRANSFER = "transfer"


class Account(Base):
    __tablename__ = "accounts"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    type: Mapped[AccountType] = mapped_column(String, nullable=False)
    balance: Mapped[float] = mapped_column(
        Numeric(precision=12, scale=2), default=0.00, nullable=False
    )

    transactions: Mapped[list["Transactions"]] = relationship(
        back_populates="account", cascade="all, delete-orphan"
    )


class TransactionGroup(Base):
    __tablename__ = "transaction_groups"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str | None] = mapped_column(String(255), nullable=True)

    transactions: Mapped[list["Transactions"]] = relationship(back_populates="group")


class Transactions(Base):
    __tablename__ = "transactions"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    account_id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id", ondelete="CASCADE"), nullable=False
    )
    group_id: Mapped[int | None] = mapped_column(
        ForeignKey("transaction_groups.id", onupdate="SET NULL"), nullable=True
    )

    title: Mapped[str] = mapped_column(String(100), nullable=False)
    transaction_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC), index=True
    )
    amount: Mapped[float] = mapped_column(
        Numeric(precision=10, scale=2), nullable=False
    )
    type: Mapped[TransactionType] = mapped_column(String, nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    payment_mode: Mapped[PaymentMode] = mapped_column(String, nullable=False)
    description: Mapped[str | None] = mapped_column(String(255), nullable=True)
    vendor: Mapped[str | None] = mapped_column(String(100), nullable=True)

    account: Mapped["Account"] = relationship(back_populates="transactions")
    group: Mapped["TransactionGroup"] = relationship(back_populates="transactions")
