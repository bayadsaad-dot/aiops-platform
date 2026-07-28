from fastapi import FastAPI
from app.api.v1.auth import router as auth_router
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.include_router(auth_router)



@app.get("/")
def root():
    return {
        "message": f"{settings.APP_NAME} API is running 🚀"
    }