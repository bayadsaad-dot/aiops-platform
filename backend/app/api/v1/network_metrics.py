from uuid import UUID

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database.deps import get_db
from app.schemas.network_metric import (
    NetworkMetricCreate,
    NetworkMetricRead,
    NetworkMetricListResponse,
)
from app.services.network_metric_service import (
    NetworkMetricService,
)

router = APIRouter(
    prefix="/api/v1/network/metrics",
    tags=["Network Metrics"],
)


@router.post(
    "/",
    response_model=NetworkMetricRead,
    status_code=201,
)
def create_network_metric(
    metric: NetworkMetricCreate,
    db: Session = Depends(get_db),
):
    return NetworkMetricService.create_metric(
        db,
        metric,
    )


@router.get(
    "/{asset_id}",
    response_model=NetworkMetricListResponse,
)
def get_network_metrics(
    asset_id: UUID,
    page: int = Query(1, ge=1),
    size: int = Query(100, ge=1),
    db: Session = Depends(get_db),
):
    metrics, total = (
        NetworkMetricService.get_asset_metrics(
            db,
            asset_id,
            page,
            size,
        )
    )

    return NetworkMetricListResponse(
        items=metrics,
        total=total,
        page=page,
        size=size,
    )