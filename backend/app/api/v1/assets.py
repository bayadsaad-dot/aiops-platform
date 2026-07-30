from uuid import UUID

from sqlalchemy.orm import Session

from app.database.deps import get_db

from app.services.asset_service import AssetService
from math import ceil
from fastapi import APIRouter, Depends, HTTPException, Query
from app.schemas.asset_summary import AssetSummary
from app.services.metric_service import MetricService
from app.enums.asset import AssetType, AssetStatus
from app.schemas.asset import (
    AssetCreate,
    AssetUpdate,
    AssetResponse,
    AssetListResponse,
)
router = APIRouter(prefix="/assets", tags=["Assets"])


@router.get("/", response_model=AssetListResponse)
def get_assets(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1),
    search: str | None = Query(None),
    asset_type: AssetType | None = Query(None),
    status: AssetStatus | None = Query(None),
):
    assets, total = AssetService.get_assets(
        db=db,
        page=page,
        size=size,
        search=search,
        asset_type=asset_type,
        status=status,
    )
    return AssetListResponse(
        items=assets,
        total=total,
        page=page,
        size=size,
        pages=ceil(total / size) if total > 0 else 0,
    )

@router.put("/{asset_id}", response_model=AssetResponse)
def update_asset(
    asset_id: UUID,
    asset: AssetUpdate,
    db: Session = Depends(get_db),
):
    try:
        return AssetService.update_asset(db, asset_id, asset)
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )

@router.get("/{asset_id}", response_model=AssetResponse)
def get_asset(
    asset_id: UUID,
    db: Session = Depends(get_db),
):
    try:
        return AssetService.get_asset_by_id(db, asset_id)
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.post("", response_model=AssetResponse)
def create_asset(
    asset: AssetCreate,
    db: Session = Depends(get_db),
):
    try:
        return AssetService.create_asset(db, asset)
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

@router.delete("/{asset_id}", status_code=204)
def delete_asset(
    asset_id: UUID,
    db: Session = Depends(get_db),
):
    try:
        AssetService.delete_asset(db, asset_id)
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )
@router.get(
    "/{asset_id}/summary",
    response_model=AssetSummary,
    summary="Get Asset Summary",
)
def get_asset_summary(
    asset_id: UUID,
    db: Session = Depends(get_db),
):
    return MetricService.get_asset_summary(
        db=db,
        asset_id=asset_id,
    )