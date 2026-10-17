from typing import Annotated

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.functions import current_user

from app.database import get_session
from app.finance.models import TransactionType
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


@router.get("", response_model=list[TransactionOut])
async def get_transactions(
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(authenticate)],
    type: TransactionType | None = Query(
        None, description="Filter by income/expese/transfer"
    ),
    category: str | None = Query(None, description="Filter by trnasction category"),
    limit: int = Query(
        20, ge=1, le=100, description="Number of logs to pull per page snapshot"
    ),
    offset: int = Query(0, ge=0, description="Number of ledger entries to skip over"),
):
    return await TransactionService(session=session).get_transactions_log(
        user_id=current_user.id,
        txt_type=type,
        category=category,
        limit=limit,
        offset=offset,
    )


@router.delete("/{transaction_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_transaction(
    transaction_id: int,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(authenticate)],
):
    return await TransactionService(session=session).delete_transaction(
        transaction_id=transaction_id, user_id=current_user.id
    )
