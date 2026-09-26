from datetime import UTC, datetime
from enum import Enum

from sqlalchemy import ARRAY, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class WorkoutSplitType(str, Enum):
    PUSH = "push"
    PULL = "pull"
    LEGS = "legs"
    CORE = "core"
    CALISTHENICS = "calisthenics"
    FULL_BODY = "full_body"


class SessionScheddule(str, Enum):
    MORNING = "morning"
    EVENING = "evening"


class ExerciseLibrary(Base):
    __tablename__ = "exercise_library"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    name: Mapped[str] = mapped_column(
        String(100), unique=True, index=True, nullable=False
    )
    targeted_muscle: Mapped[str] = mapped_column(String(50), index=True, nullable=False)
    recovery_time_hours: Mapped[int] = mapped_column(
        Integer, default=48, nullable=False
    )
    valid_splits: Mapped[list[str]] = mapped_column(ARRAY(String), nullable=False)

    logged_instances: Mapped[list["ExerciseLog"]] = relationship(
        back_populates="exercise_meta"
    )


class WorkoutSession(Base):
    __tablename__ = "wokout_sessions"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), onupdate="CASCADE", nullable=False
    )
    split_type: Mapped[WorkoutSplitType | None] = mapped_column(
        String, nullable=True, index=True, default=None
    )
    schedule: Mapped[SessionScheddule] = mapped_column(
        String, nullable=False, index=True
    )
    title: Mapped[str] = mapped_column(String(100), default="Daily Workout")
    date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC)
    )

    exercises: Mapped[list["ExerciseLog"]] = relationship(
        back_populates="session", cascade="all, delete-orphan", lazy="selectin"
    )


class ExerciseLog(Base):
    __tablename__ = "workout_exercise_logs"

    session_id: Mapped[int] = mapped_column(
        ForeignKey("wokout_sessions.id", ondelete="CASCADE"), nullable=False
    )
    exercise_name: Mapped[str] = mapped_column(
        ForeignKey("exercise_library.name", onupdate="CASCADE"), nullable=False
    )
    sets: Mapped[int] = mapped_column(Integer, nullable=False)
    reps: Mapped[int] = mapped_column(Integer, nullable=False)
    weight: Mapped[int | None] = mapped_column(Integer, default=None, nullable=True)

    exercise_meta: Mapped["ExerciseLibrary"] = relationship(
        back_populates="logged_instances", lazy="joined"
    )
    session: Mapped["WorkoutSession"] = relationship(back_populates="exercises")
