from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import TransactionGroup
from ..schemas import TransactionGroupCreate, TransactionGroupUpdate


class TransactionGroupService:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_all_groups(self, user_id: int) -> list[TransactionGroup]:
        result = await self._session.execute(
            select(TransactionGroup)
            .where(TransactionGroup.user_id == user_id)
            .order_by(TransactionGroup.name.asc())
        )
        return result.scalars().all()

    async def save_group(
        self, user_id: int, transaction_group_details: TransactionGroupCreate
    ) -> TransactionGroup:
        result = await self._session.execute(
            select(TransactionGroup).where(
                TransactionGroup.user_id == user_id,
                TransactionGroup.name == transaction_group_details.name,
            )
        )
        existing_group = result.scalars().first()
        if existing_group:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"An Transaction Group named {transaction_group_details.name} is already exists",
            )

        new_transaction_group = TransactionGroup(
            **transaction_group_details.model_dump(), user_id=user_id
        )
        self._session.add(new_transaction_group)
        await self._session.commit()
        await self._session.refresh(new_transaction_group)
        return new_transaction_group

    async def update_transaction_group(
        self,
        transaction_group_details: TransactionGroupUpdate,
        transaction_group_id: int,
        user_id: int,
    ) -> TransactionGroup:
        result = await self._session.execute(
            select(TransactionGroup).where(TransactionGroup.id == transaction_group_id)
        )
        transaction_group = result.scalars().first()
        if not transaction_group:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Transaction group not found to delete",
            )
        if transaction_group.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized to update this transaction group",
            )
        update_data = transaction_group_details.model_dump(exclude_none=True)
        for field, value in update_data.items():
            setattr(transaction_group, field, value)

        await self._session.commit()
        await self._session.refresh(transaction_group)

        return transaction_group

    async def delete_transaction_group(
        self, transaction_group_id: int, user_id: int
    ) -> None:
        result = await self._session.execute(
            select(TransactionGroup).where(TransactionGroup.id == transaction_group_id)
        )
        transaction_group = result.scalars().first()
        if not transaction_group:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Transaction group not found to delete",
            )
        if transaction_group.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized to delete this transaction group",
            )

        await self._session.delete(transaction_group)
        await self._session.commit()
