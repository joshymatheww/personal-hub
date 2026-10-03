from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.middlewares.auth import authenticate
from app.models import User

from ..schemas import AccountCreate, AccountOut
from ..services.account_service import AccountService

router = APIRouter()


@router.get("", response_model=list[AccountOut])
async def get_all_account(
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(authenticate)],
):
    return await AccountService(session=session).get_all_accounts(
        user_id=current_user.id
    )


@router.post("", response_model=AccountOut)
async def create_account(
    payload: AccountCreate,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(authenticate)],
):
    return await AccountService(session=session).save_account(
        user_id=current_user.id, account_details=payload
    )
