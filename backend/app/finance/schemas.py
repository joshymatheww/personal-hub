from datetime import UTC, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

from app.finance.models import AccountType, PaymentMode, TransactionType


class AccountBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    type: AccountType
    balance: Decimal = Field(..., max_digits=12, decimal_places=2, ge=0)


class AccountCreate(AccountBase):
    pass


class AccountUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    type: AccountType | None = Field(default=None)
    balance: Decimal | None = Field(default=None, max_digits=12, decimal_places=2, ge=0)


class AccountOut(AccountBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class TransactionGroupBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=255)


class TransactionGroupCreate(TransactionGroupBase):
    pass


class TransactionGroupOut(TransactionGroupBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class TransactionBase(BaseModel):
    account_id: int
    group_id: int | None = Field(default=None)
    title: str = Field(min_length=1, max_length=100)
    transaction_time: datetime = Field(default_factory=lambda: datetime.now(UTC))
    amount: Decimal = Field(..., max_digits=10, decimal_places=2, gt=0)
    type: TransactionType
    category: str = Field(..., min_length=1, max_length=50)
    payment_mode: PaymentMode
    description: str | None = Field(default=None, max_length=255)
    vendor: str | None = Field(default=None, max_length=100)


class TransactionCreate(TransactionBase):
    pass


class TransactionOut(TransactionBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class FinanceMetaDataOut(BaseModel):
    account_types: list[str]
    payment_modes: list[str]
    transaction_types: list[str]
    categories: dict[str, list[str]]
