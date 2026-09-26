from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.middlewares.auth import authenticate
from app.models import User

from .models import WorkoutSplitType
from .routers import library
from .schemas import WorkoutsMetaData
from .services.library_service import LibraryService

router = APIRouter()

router.include_router(library.router, prefix="/library", tags=["Exercise Library"])


@router.get("/meta-data", response_model=WorkoutsMetaData, tags=["Workouts Metadata"])
async def get_worksouts_meta_data(
    session: Annotated[AsyncSession, Depends(get_session)],
    current_user: Annotated[User, Depends(authenticate)],
):
    muscle_groups = await LibraryService(session=session).get_muscle_groups(
        user_id=current_user.id
    )
    return WorkoutsMetaData(
        muscle_groups=muscle_groups,
        split_types=[
            {"label": type.name, "value": type.value} for type in WorkoutSplitType
        ],
    )
