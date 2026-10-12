from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.middlewares.auth import authenticate
from app.models import User

from ..schemas import TransactionCreate, TransactionOut
from ..services.transaction_service import TransactionService

router = APIRouter()


@router.post("", response_model=TransactionOut)
async def create_transaction(
    payload: TransactionCreate,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(authenticate)],
):
    return await TransactionService(session=session).save_transaction(
        transaction_details=payload, user_id=current_user.id
    )
