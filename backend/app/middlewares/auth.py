from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.helpers import verify_token
from app.auth.schemas import UserResponse
from app.database import get_session
from app.models import User

securuty_scheme = HTTPBearer()

AUTH_PREFIX = "Bearer"


async def authenticate(
    session: Annotated[AsyncSession, Depends(get_session)],
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(securuty_scheme)],
) -> UserResponse:
    auth_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
    )
    authorization = credentials.scheme

    if not auth_exception:
        raise auth_exception
    if not authorization.startswith(AUTH_PREFIX):
        raise auth_exception

    token = credentials.credentials
    user_id = verify_token(token=token)

    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authorization": "Bearer"},
        )
    try:
        user_id = int(user_id)
    except (TypeError, ValueError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authorization": "Bearer"},
        )
    result = await session.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="user not found",
            headers={"WWW-Authorization": "Bearer"},
        )
    return user
