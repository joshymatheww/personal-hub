from fastapi import FastAPI

from app.auth import router as authRouter
from app.workouts import router as workoutRouter

app = FastAPI(title="Personal Dashboard API")


app.include_router(authRouter.router, prefix="/api/auth", tags=["Auth"])
app.include_router(workoutRouter.router, prefix="/api/workouts")


@app.get("/healthz")
def health_check():
    return {"status": "OK"}
