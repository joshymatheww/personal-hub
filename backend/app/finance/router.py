from typing import Annotated

from fastapi import APIRouter, Depends

from app.middlewares.auth import authenticate
from app.models import User

from .models import AccountType, PaymentMode, TransactionType
from .routers import account
from .schemas import FinanceMetaDataOut

router = APIRouter()

CORE_CATEGORIES = {
    TransactionType.INCOME.value: [
        "Salary / Primary Income",
        "Freelance / Side Income",
        "Investment Returns",
        "Gifts & Others",
    ],
    TransactionType.EXPENSE.value: [
        "Food & Dining",
        "Groceries",
        "Fuel",
        "Bus Fare",
        "Auto Fare",
        "Train Fare",
        "Flight & Long Disatnce Travel",
        "Mobile Recharges",
        "WiFi / Broadband Recharges",
        "OTT Recharges (Netflix, Prime etc.)",
        "Electricity & Utilities",
        "Scholl Fees",
        "School Bus Fees",
        "Books & Learning Materials",
        "Online Shopping",
        "Offline Shopping / Retail",
        "Apparel & Clothing",
        "Medical & Hospital Expenses",
        "Medicines & Pharmacy",
    ],
    TransactionType.TRANSFER.value: ["Account Transfer"],
}


router.include_router(account.router, prefix="/accounts", tags=["Accounts", "Finance"])


@router.get("/metadata", response_model=FinanceMetaDataOut, tags=["Finance"])
async def get_finanace_metadata(current_user: Annotated[User, Depends(authenticate)]):
    return {
        "account_types": [e.value for e in AccountType],
        "payment_modes": [e.value for e in PaymentMode],
        "transaction_types": [e.value for e in TransactionType],
        "categories": CORE_CATEGORIES,
    }
