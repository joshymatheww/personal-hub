from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.middlewares.auth import authenticate
from app.models import User

from ..schemas import (
    TransactionGroupCreate,
    TransactionGroupOut,
    TransactionGroupUpdate,
)
from ..services.transaction_group_service import TransactionGroupService

router = APIRouter()


@router.get("", response_model=list[TransactionGroupOut])
async def get_all_groups(
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(authenticate)],
):
    return await TransactionGroupService(session=session).get_all_groups(
        user_id=current_user.id
    )


@router.post("", response_model=TransactionGroupOut)
async def create_transaction_group(
    payload: TransactionGroupCreate,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(authenticate)],
):
    return await TransactionGroupService(session=session).save_group(
        user_id=current_user.id, transaction_group_details=payload
    )


@router.patch("/{transaction_group_id}", response_model=TransactionGroupOut)
async def update_transaction_group(
    transaction_group_id: int,
    payload: TransactionGroupUpdate,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(authenticate)],
):
    return await TransactionGroupService(session=session).update_transaction_group(
        transaction_group_details=payload,
        transaction_group_id=transaction_group_id,
        user_id=current_user.id,
    )


@router.delete("/{transaction_group_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_transaction_group(
    transaction_group_id: int,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(authenticate)],
):
    await TransactionGroupService(session=session).delete_transaction_group(
        transaction_group_id=transaction_group_id, user_id=current_user.id
    )
