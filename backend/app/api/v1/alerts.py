from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database.deps import get_db

from app.services.alert_service import AlertService

from app.schemas.alert import (
    AlertRead,
    AlertListResponse,
)

router = APIRouter(
    prefix="/api/v1/alerts",
    tags=["Alerts"],
)


@router.get(
    "/",
    response_model=AlertListResponse,
)
def get_alerts(
    page: int = Query(1, ge=1),
    size: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):

    alerts, total = AlertService.get_alerts(
        db=db,
        page=page,
        size=size,
    )

    return AlertListResponse(
        items=alerts,
        total=total,
        page=page,
        size=size,
    )


@router.get(
    "/open",
    response_model=list[AlertRead],
)
def get_open_alerts(
    db: Session = Depends(get_db),
):

    return AlertService.get_open_alerts(db)