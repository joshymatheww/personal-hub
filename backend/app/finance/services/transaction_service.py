from decimal import Decimal

from fastapi import HTTPException, status
from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Account, Transactions, TransactionType
from ..schemas import TransactionCreate


class TransactionService:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def save_transaction(
        self, transaction_details: TransactionCreate, user_id: int
    ) -> Transactions:
        async with self._session.begin():
            result = await self._session.execute(
                select(Account).where(
                    Account.id == transaction_details.account_id,
                    Account.user_id == user_id,
                )
            )
            source_account = result.scalars().first()

            if not source_account:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Source account not found",
                )
            # 2. Process account modifications based on the transaction type parameter
            if transaction_details.type == TransactionType.INCOME:
                source_account.balance += transaction_details.amount

            elif transaction_details.type == TransactionType.EXPENSE:
                source_account.balance -= transaction_details.amount

            elif transaction_details.type == TransactionType.TRANSFER:
                if not transaction_details.to_account:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,  # Changed to 400 Bad Request
                        detail="Please select an account to transfer",
                    )

                # Fetch the destination target account
                dest_result = await self._session.execute(
                    select(Account).where(
                        Account.id == transaction_details.to_account,
                        Account.user_id == user_id,
                    )
                )
                destination_account = dest_result.scalars().first()
                if not destination_account:
                    raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail="Destination account not found",
                    )

                # Atomic transfer balance movement calculations
                source_account.balance -= transaction_details.amount
                destination_account.balance += transaction_details.amount

            # 3. Instantiate and persist the transaction row record
            new_transaction = Transactions(
                **transaction_details.model_dump(exclude_none=True), user_id=user_id
            )
            self._session.add(new_transaction)

        await self._session.refresh(new_transaction)
        return new_transaction

    async def delete_transaction(self, transaction_id: int, user_id: int) -> None:
        async with self._session.begin():
            # 1. Fetch the target transaction row to verify ownership
            result = await self._session.execute(
                select(Transactions).where(
                    Transactions.id == transaction_id, Transactions.user_id == user_id
                )
            )
            transaction = result.scalars().first()
            if not transaction:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Transaction not found",
                )
            # 2. Fetch the primary source account linked to the log
            result = await self._session.execute(
                select(Account).where(
                    Account.id == transaction.account_id, Account.user_id == user_id
                )
            )
            source_account = result.scalars().first()
            if not source_account:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="Account not found"
                )

            # Force clean Decimal parsing to safeguard mathematical accuracy
            txt_amount = Decimal(str(transaction.amount))

            # 3. Reversing calculation logic matching transaction execution profiles
            if transaction.type == TransactionType.INCOME:
                source_account.balance = (
                    Decimal(str(source_account.balance)) - txt_amount
                )
            elif transaction.type == TransactionType.EXPENSE:
                source_account.balance = (
                    Decimal(str(source_account.balance)) + txt_amount
                )
            elif transaction.type == TransactionType.TRANSFER:
                if not transaction.to_account:
                    raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail="Corrupted transter log. Missing destination account",
                    )
                result = await self._session.execute(
                    select(Account).where(
                        Account.id == transaction.to_account, Account.user_id == user_id
                    )
                )
                destination_account = result.scalars().first()
                if not destination_account:
                    raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail="Destination account not found",
                    )
                # Put money back in source, remove money from destination
                source_account.balance = (
                    Decimal(str(source_account.balance)) + txt_amount
                )
                destination_account.balance = (
                    Decimal(str(destination_account.balance)) - txt_amount
                )
        # 4. Remove the log row from the ledger table completely
        await self._session.delete(transaction)

    async def get_transactions_log(
        self,
        user_id: int,
        limit: int,
        offset: int,
        txt_type: TransactionType | None,
        category: str | None,
    ) -> list[Transactions]:
        # Formulate the base selection criteria targeting user ownership
        query = select(Transactions).where(Transactions.user_id == user_id)

        # Dynamically applies filters for the transactions
        if txt_type:
            query = query.where(Transactions.type == txt_type.value)
        if category:
            query = query.where(Transactions.category == category)

        # Sort transactions chronologically
        query.order_by(
            desc(Transactions.transaction_time), desc(Transactions.id)
        ).limit(limit).offset(offset)

        result = await self._session.execute(query)
        return list(result.scalars().all())
