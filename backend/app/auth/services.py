from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User

from .helpers import create_access_token, hash_password, verify_password
from .schemas import TokenRequest, TokenResponse, UserCreate, UserResponse


class AuthService:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def signup(self, user_detail: UserCreate) -> UserResponse:
        result = await self._session.execute(
            select(User).where(User.email == user_detail.email)
        )
        exsiting_user = result.scalars().first()
        if exsiting_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User already exists, Please login",
            )
        user = User(
            **user_detail.model_dump(exclude={"password"}, exclude_none=True),
            hashed_password=hash_password(user_detail.password),
        )

        self._session.add(user)
        await self._session.commit()
        await self._session.refresh(user)

        return user

    async def login(self, login_request: TokenRequest) -> TokenResponse:
        result = await self._session.execute(
            select(User).where(User.email == login_request.email)
        )
        user = result.scalars().first()
        if user and verify_password(login_request.password, user.hashed_password):
            access_token = create_access_token(data={"sub": str(user.id)})
            return TokenResponse(access_token=access_token, token_type="bearer")
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
            )
