from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Account, AccountType
from ..schemas import AccountCreate, AccountUpdate


class AccountService:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_all_accounts(self, user_id: int) -> list[Account]:
        result = await self._session.execute(
            select(Account)
            .where(Account.user_id == user_id)
            .order_by(Account.name.asc())
        )
        return result.scalars().all()

    async def save_account(
        self, user_id: int, account_details: AccountCreate
    ) -> Account:
        result = await self._session.execute(
            select(Account).where(
                Account.user_id == user_id, Account.name == account_details.name
            )
        )
        existing_account = result.scalars().first()
        if existing_account:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"An account named {account_details.name} is already exists",
            )

        new_account = Account(**account_details.model_dump(), user_id=user_id)
        self._session.add(new_account)
        await self._session.commit()
        await self._session.refresh(new_account)
        return new_account

    async def update_account(
        self, account_details: AccountUpdate, account_id: int, user_id: int
    ) -> Account:
        result = await self._session.execute(
            select(Account).where(Account.id == account_id)
        )
        account = result.scalars().first()
        if not account:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Account not found to delete",
            )
        if account.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized to update this account",
            )
        update_data = account_details.model_dump(exclude_none=True)
        for field, value in update_data.items():
            setattr(account, field, value)

        await self._session.commit()
        await self._session.refresh(account)

        return account

    async def delete_account(self, account_id: int, user_id: int) -> None:
        result = await self._session.execute(
            select(Account).where(Account.id == account_id)
        )
        account = result.scalars().first()
        if not account:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Account not found to delete",
            )
        if account.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized to delete this account",
            )

        await self._session.delete(account)
        await self._session.commit()
