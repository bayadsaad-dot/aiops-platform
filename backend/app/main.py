from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.auth import router as auth_router
from app.api.v1.metrics import router as metric_router
from app.api.v1.assets import router as asset_router
from app.dashboard.router import router as dashboard_router
from app.core.config import settings
from app.api.v1.network import router as network_router
from app.api.v1.network_metrics import (
    router as network_metric_router,
)
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dashboard_router)
app.include_router(auth_router)
app.include_router(asset_router)
app.include_router(metric_router)
app.include_router(network_router)
app.include_router(network_metric_router)
@app.get("/")
def root():
    return {
        "message": f"{settings.APP_NAME} API is running 🚀"
    }