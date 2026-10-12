from datetime import UTC, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field, field_validator
from pydantic_core import PydanticCustomError

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


class TransactionGroupUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=255)


class TransactionGroupOut(TransactionGroupBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class TransactionBase(BaseModel):
    account_id: int
    to_account: int | None = Field(default=None)
    group_id: int | None = Field(default=None)
    title: str = Field(
        min_length=1,
        max_length=100,
    )
    transaction_time: datetime = Field(default_factory=lambda: datetime.now(UTC))
    amount: Decimal = Field(..., max_digits=10, decimal_places=2, gt=0)
    type: TransactionType
    category: str
    payment_mode: PaymentMode
    description: str | None = Field(default=None, max_length=255)
    vendor: str | None = Field(default=None, max_length=100)

    @field_validator("account_id")
    @classmethod
    def validate_account_id(cls, value: int) -> int:
        if value <= 0:
            raise PydanticCustomError("greater_than", "Please select an Account")
        return value

    @field_validator("amount", mode="before")
    @classmethod
    def validate_amount(cls, value: int) -> int:
        if value <= 0:
            raise PydanticCustomError(
                "greater_than", "The transaction amount must be greather than 0"
            )
        return value

    @field_validator("title", mode="before")
    @classmethod
    def validate_title(cls, value: str) -> str:
        if len(value) <= 3:
            raise PydanticCustomError(
                "string_too_short", "Please enter valid transaction title"
            )
        return value

    @field_validator("category", mode="before")
    @classmethod
    def validate_category(cls, value: str) -> str:
        if len(value) <= 3:
            raise PydanticCustomError("string_too_short", "Please select a category")
        return value

    @field_validator("payment_mode", mode="before")
    @classmethod
    def validate_payment_mode(cls, value: str) -> str:
        if len(value) <= 2:
            raise PydanticCustomError(
                "string_too_short", "Please select the payment mode"
            )
        return value


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
