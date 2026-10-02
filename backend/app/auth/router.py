from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.database import get_session
from app.middlewares.auth import authenticate
from app.models import User

from .schemas import TokenRequest, TokenResponse, UserCreate, UserResponse
from .services import AuthService

router = APIRouter()


@router.post("/create_admin", response_model=UserResponse)
async def create_admin(session: Annotated[AsyncSession, Depends(get_session)]):
    user_details = UserCreate(
        first_name=settings.admin_first_name,
        last_name=settings.admin_last_name,
        email=settings.admin_email,
        password=settings.admin_password,
    )
    return await AuthService(session=session).signup(user_detail=user_details)


@router.post("/token", response_model=TokenResponse)
async def get_access_token(
    payload: TokenRequest, session: Annotated[AsyncSession, Depends(get_session)]
):
    return await AuthService(session=session).login(login_request=payload)


@router.get("/me", response_model=UserResponse)
async def get_current_user(current_user: Annotated[User, Depends(authenticate)]):
    return current_user
