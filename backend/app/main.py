from fastapi import FastAPI

from app.auth import router as authRouter

app = FastAPI(title="Personal Dashboard API")


app.include_router(authRouter.router, prefix="/api/auth", tags=["auth"])


@app.get("/healthz")
def health_check():
    return {"status": "OK"}
