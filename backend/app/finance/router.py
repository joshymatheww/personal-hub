from fastapi import APIRouter

from .routers import account

router = APIRouter()

router.include_router(account.router, prefix="/accounts", tags=["Accounts"])
