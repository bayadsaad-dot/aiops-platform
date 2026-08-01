from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dashboard.schema import DashboardSummary
from app.dashboard.service import DashboardService
from app.database.deps import get_db

router = APIRouter(
    prefix="/api/v1/dashboard",
    tags=["Dashboard"],
)


@router.get(
    "/",
    response_model=DashboardSummary,
)
def get_dashboard_summary(
    db: Session = Depends(get_db),
):
    return DashboardService.get_summary(db)