from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.deps import get_db

from app.schemas.dashboard import DashboardOverview
from app.schemas.dashboard_metrics import DashboardMetrics

from app.services.dashboard_service import DashboardService
from app.services.dashboard_metrics_service import DashboardMetricsService

router = APIRouter(
    prefix="/api/v1/dashboard",
    tags=["Dashboard"],
)


@router.get(
    "/overview",
    response_model=DashboardOverview,
)
def overview(
    db: Session = Depends(get_db),
):
    return DashboardService.get_overview(db)


@router.get(
    "/metrics",
    response_model=DashboardMetrics,
)
def metrics(
    db: Session = Depends(get_db),
):
    return DashboardMetricsService.get_metrics(db)