from typing import Annotated

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.middlewares.auth import authenticate
from app.models import User

from ..models import WorkoutSplitType
from ..schemas import ExerciseLibraryCreate, ExerciseLibraryOut
from ..services.library_service import LibraryService

router = APIRouter()


@router.get("", response_model=list[ExerciseLibraryOut])
async def get_all_exercises(
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(authenticate)],
):
    return await LibraryService(session=session).get_all_exercises(
        user_id=current_user.id
    )


@router.post("", response_model=ExerciseLibraryOut, status_code=status.HTTP_201_CREATED)
async def create_new_exercise(
    payload: ExerciseLibraryCreate,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(authenticate)],
):
    return await LibraryService(session=session).save_exercise(
        exercise_details=payload, user_id=current_user.id
    )


@router.get("/by-muscle", response_model=list[ExerciseLibraryOut])
async def get_exercises_by_muscle_groups(
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(authenticate)],
    muscles: list[str] = Query(..., description="List of targeted muscle groups"),
):
    return await LibraryService(session=session).get_exercise_by_muscle_groups(
        muscle_groups=muscles, user_id=current_user.id
    )


@router.get("/{exercise_id}", response_model=ExerciseLibraryOut)
async def get_exercise_by_id(
    exercise_id: int,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(authenticate)],
):
    return await LibraryService(session=session).get_exercise(
        id=exercise_id, user_id=current_user.id
    )


@router.put("/{exercise_id}", response_model=ExerciseLibraryOut)
async def update_exercise(
    exercise_id: int,
    payload: ExerciseLibraryCreate,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(authenticate)],
):
    return await LibraryService(session=session).update_exercise(
        exercise_id=exercise_id, exercise_details=payload, user_id=current_user.id
    )


@router.delete("/{exercise_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_exercise(
    exercise_id: int,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(authenticate)],
):
    await LibraryService(session=session).delete_exercise(
        exercise_id=exercise_id, user_id=current_user.id
    )


@router.get("/by-split/{split_type}", response_model=list[ExerciseLibraryOut])
async def get_exercises_by_split(
    split_type: WorkoutSplitType,
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(authenticate)],
):
    return await LibraryService(session=session).get_exercise_by_split(
        split_type=split_type, user_id=current_user.id
    )
