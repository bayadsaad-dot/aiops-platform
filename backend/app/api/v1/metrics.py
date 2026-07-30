from uuid import UUID

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database.deps import get_db
from app.schemas.metric import (
    MetricCreate,
    MetricRead,
    MetricListResponse,
)
from app.services.metric_service import MetricService

router = APIRouter(
    prefix="/api/v1/metrics",
    tags=["Metrics"],
)


@router.post(
    "/",
    response_model=MetricRead,
    status_code=201,
    summary="Create Metric",
    description="Receive monitoring metrics from an agent and store them in the database.",
)
def create_metric(
    metric: MetricCreate,
    db: Session = Depends(get_db),
):
    return MetricService.create_metric(db, metric)


@router.get(
    "/asset/{asset_id}",
    response_model=MetricListResponse,
    summary="Get Asset Metrics",
    description="Return paginated metrics for an asset with optional time filtering.",
)
def get_asset_metrics(
    asset_id: UUID,
    page: int = Query(
        default=1,
        ge=1,
        description="Page number",
    ),
    size: int = Query(
        default=50,
        ge=1,
        le=500,
        description="Items per page",
    ),
    period: str | None = Query(
        default=None,
        pattern="^(1h|24h|7d|30d)$",
        description="Filter metrics by period: 1h, 24h, 7d or 30d",
    ),
    db: Session = Depends(get_db),
):
    metrics, total = MetricService.get_asset_metrics(
        db=db,
        asset_id=asset_id,
        page=page,
        size=size,
        period=period,
    )

    return MetricListResponse(
        items=metrics,
        total=total,
        page=page,
        size=size,
    )