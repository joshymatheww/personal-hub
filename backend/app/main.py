from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.auth import router as authRouter
from app.finance import router as fiananceRouter
from app.workouts import router as workoutRouter

from .config import settings
from .database import engine


@asynccontextmanager
async def lifespan(_app: FastAPI):
    yield
    await engine.dispose()


app = FastAPI(title="Personal Dashboard API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.get_cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(authRouter.router, prefix="/api/auth", tags=["Auth"])
app.include_router(workoutRouter.router, prefix="/api/workouts")
app.include_router(fiananceRouter.router, prefix="/api/finance")


@app.get("/healthz")
def health_check():
    return {"status": "OK"}
