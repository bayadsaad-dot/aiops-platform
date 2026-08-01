from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.deps import get_db
from app.schemas.network_sync import NetworkSyncRequest
from app.services.network_service import NetworkService

router = APIRouter(
    prefix="/api/v1/network",
    tags=["Network"],
)


@router.post("/interfaces/sync")
def sync_interfaces(
    data: NetworkSyncRequest,
    db: Session = Depends(get_db),
):
    return NetworkService.sync_interfaces(
        db,
        data,
    )