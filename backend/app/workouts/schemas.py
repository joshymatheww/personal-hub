from datetime import UTC, datetime

from pydantic import BaseModel, ConfigDict, Field

from .models import SessionScheddule, WorkoutSplitType


class ExerciseLibraryBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    targeted_muscle: str = Field(..., min_length=1, max_length=50)
    recovery_time_hours: int = Field(48, gt=0)
    valid_splits: list[WorkoutSplitType] = Field(..., min_length=1)


class ExerciseLibraryCreate(ExerciseLibraryBase):
    pass


class ExerciseLibraryOut(ExerciseLibraryBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class ExerciseLogBase(BaseModel):
    exercise_name: str
    sets: int = Field(..., gt=0)
    reps: int = Field(..., gt=0)
    weight: float | None = Field(default=None, gt=0)


class ExerciseLogCreate(ExerciseLogBase):
    pass


class ExerciseLogOut(ExerciseLogBase):
    id: int
    session_id: int
    exercise_meta: ExerciseLibraryOut

    model_config = ConfigDict(from_attributes=True)


class WorkoutSessionBase(BaseModel):
    split_type: WorkoutSplitType
    schedule: SessionScheddule
    title: str = Field("Daily Workout", max_length=100)
    notes: str | None = Field(default=None)
    date: datetime = Field(default_factory=lambda: datetime.now(UTC))


class WorkoutSessionCreate(WorkoutSessionBase):
    exercises: list[ExerciseLogCreate] = []


class WorkoutSessionOut(WorkoutSessionBase):
    id: int
    user_id: int
    exercises: list[ExerciseLogOut]

    model_config = ConfigDict(from_attributes=True)


class WorkoutsMetaData(BaseModel):
    muscle_groups: list[str]
    split_types: list[dict]
