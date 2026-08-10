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


# -----------------------------
# Create Network Metric
# -----------------------------
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
        db=db,
        data=metric,
    )


# -----------------------------
# Latest Network Metrics
# IMPORTANT:
# This endpoint MUST be before /{asset_id}
# -----------------------------
@router.get(
    "/latest",
    response_model=NetworkMetricListResponse,
)
def get_latest_metrics(
    limit: int = Query(
        default=20,
        ge=1,
        le=200,
    ),
    db: Session = Depends(get_db),
):
    metrics = NetworkMetricService.get_latest(
        db=db,
        limit=limit,
    )

    return NetworkMetricListResponse(
        items=metrics,
        total=len(metrics),
        page=1,
        size=limit,
    )


# -----------------------------
# Metrics By Asset
# -----------------------------
@router.get(
    "/{asset_id}",
    response_model=NetworkMetricListResponse,
)
def get_network_metrics(
    asset_id: UUID,
    page: int = Query(
        default=1,
        ge=1,
    ),
    size: int = Query(
        default=100,
        ge=1,
    ),
    db: Session = Depends(get_db),
):
    metrics, total = (
        NetworkMetricService.get_asset_metrics(
            db=db,
            asset_id=asset_id,
            page=page,
            size=size,
        )
    )

    return NetworkMetricListResponse(
        items=metrics,
        total=total,
        page=page,
        size=size,
    )