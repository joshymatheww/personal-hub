from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import ExerciseLibrary, WorkoutSplitType
from ..schemas import ExerciseLibraryCreate


class LibraryService:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_all_exercises(self, user_id: int) -> list[ExerciseLibrary]:
        result = await self._session.execute(
            select(ExerciseLibrary)
            .where(ExerciseLibrary.user_id == user_id)
            .order_by(ExerciseLibrary.name.asc())
        )
        return result.scalars().all()

    async def save_exercise(
        self, exercise_details: ExerciseLibraryCreate, user_id: int
    ) -> ExerciseLibrary:
        # check if an extercise with this name already exists
        result = await self._session.execute(
            select(ExerciseLibrary).where(ExerciseLibrary.name == exercise_details.name)
        )
        existing_library = result.scalars().first()
        if existing_library:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"An exercise named {exercise_details.name} already exists in the library",
            )

        new_exercise = ExerciseLibrary(**exercise_details.model_dump(), user_id=user_id)
        self._session.add(new_exercise)
        await self._session.commit()
        await self._session.refresh(new_exercise)
        return new_exercise

    async def get_exercise(self, id: int, user_id: int) -> ExerciseLibrary:
        result = await self._session.execute(
            select(ExerciseLibrary).where(
                ExerciseLibrary.id == id, ExerciseLibrary.user_id == user_id
            )
        )
        exercise = result.scalars().first()
        if not exercise:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Exercise not found in the library",
            )
        return exercise

    async def update_exercise(
        self, exercise_details: ExerciseLibraryCreate, exercise_id: int, user_id: int
    ) -> ExerciseLibrary:
        result = await self._session.execute(
            select(ExerciseLibrary).where(ExerciseLibrary.id == exercise_id)
        )
        exercise = result.scalars().first()
        if not exercise:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Exercise not found to update",
            )
        if exercise.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized to update this exercise",
            )
        update_data = exercise_details.model_dump(exclude_none=True)
        for field, value in update_data.items():
            setattr(exercise, field, value)

        await self._session.commit()
        await self._session.refresh(exercise)

        return exercise

    async def delete_exercise(self, exercise_id: int, user_id: int) -> None:
        result = await self._session.execute(
            select(ExerciseLibrary).where(ExerciseLibrary.id == exercise_id)
        )
        exercise = result.scalars().first()
        if not exercise:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Exercise not found to delete",
            )
        if exercise.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized to delete this exercise",
            )

        await self._session.delete(exercise)
        await self._session.commit()

    async def get_exercise_by_split(
        self, split_type: WorkoutSplitType, user_id: int
    ) -> list[ExerciseLibrary]:
        result = await self._session.execute(
            select(ExerciseLibrary)
            .where(
                ExerciseLibrary.user_id == user_id,
                ExerciseLibrary.valid_splits.any(split_type.value),
            )
            .order_by(ExerciseLibrary.name.asc())
        )
        return result.scalars().all()

    async def get_exercise_by_muscle_groups(
        self, muscle_groups: list[str], user_id: int
    ) -> list[ExerciseLibrary]:
        result = await self._session.execute(
            select(ExerciseLibrary)
            .where(
                ExerciseLibrary.user_id == user_id,
                ExerciseLibrary.targeted_muscle.in_(muscle_groups),
            )
            .order_by(ExerciseLibrary.name.asc())
        )
        return result.scalars().all()

    async def get_muscle_groups(self, user_id: int) -> list[str]:
        result = await self._session.execute(
            select(ExerciseLibrary.targeted_muscle)
            .where(ExerciseLibrary.user_id == user_id)
            .distinct()
            .order_by(ExerciseLibrary.targeted_muscle.asc())
        )
        return list(result.scalars().all())
