from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1.incidents import router as incident_router
from app.api.v1 import alerts
from app.api.v1 import dashboard
from app.api.v1.websocket import router as websocket_router
from app.api.v1.auth import router as auth_router
from app.api.v1.assets import router as asset_router
from app.api.v1.metrics import router as metric_router
from app.models.website import Website
from app.api.v1.network import router as network_router
from app.api.v1.processes import router as process_router
from app.api.v1.heartbeat import router as heartbeat_router
from app.scheduler.website_scheduler import (
    start_website_scheduler,
)
from app.api.v1.heartbeat_monitor import (
    router as heartbeat_monitor_router,
)
from app.api.v1.network_metrics import (
    router as network_metric_router,
)

from app.dashboard.router import router as dashboard_router
from app.api.v1.websites import router as website_router
from app.scheduler.heartbeat_scheduler import (
    start_scheduler,
)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

@app.on_event("startup")
def startup():
    start_scheduler()
    start_website_scheduler()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(heartbeat_router)
app.include_router(heartbeat_monitor_router)
app.include_router(dashboard.router)
app.include_router(alerts.router)
app.include_router(dashboard_router)
app.include_router(auth_router)
app.include_router(asset_router)
app.include_router(metric_router)
app.include_router(incident_router)
app.include_router(network_router)
app.include_router(network_metric_router)
app.include_router(process_router)
app.include_router(website_router)
app.include_router(websocket_router)
@app.get("/")
def root():
    return {
        "message": f"{settings.APP_NAME} API is running 🚀"
    }