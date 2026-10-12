from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Account, Transactions, TransactionType
from ..schemas import TransactionCreate


class TransactionService:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def save_transaction(
        self, transaction_details: TransactionCreate, user_id: int
    ) -> Transactions:
        result = await self._session.execute(
            select(Account).where(
                Account.id == transaction_details.account_id, Account.user_id == user_id
            )
        )
        source_account = result.scalars().first()

        if not source_account:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Source account not found"
            )

        if transaction_details.type == TransactionType.INCOME:
            source_account.balance += transaction_details.amount
        elif transaction_details.type == TransactionType.EXPENSE:
            source_account.balance -= transaction_details.amount
        elif transaction_details.type == TransactionType.TRANSFER:
            if not transaction_details.to_account:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Please select an account to transfer",
                )
            result = await self._session.execute(
                select(Account).where(
                    Account.id == transaction_details.to_account,
                    Account.user_id == user_id,
                )
            )
            destination_account = result.scalars().first()
            if not destination_account:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Destination account not found",
                )
            source_account.balance -= transaction_details.amount
            destination_account.balance += transaction_details.amount

        new_transaction = Transactions(
            **transaction_details.model_dump(exclude_none=True), user_id=user_id
        )
        self._session.add(new_transaction)
        await self._session.commit()
        await self._session.refresh(new_transaction)
        return new_transaction
