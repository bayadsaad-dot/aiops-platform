from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.deps import get_db
from app.services.heartbeat_monitor_service import (
    HeartbeatMonitorService,
)

router = APIRouter(
    prefix="/api/v1/heartbeat-monitor",
    tags=["Heartbeat Monitor"],
)


@router.post("/check")
def check_heartbeats(
    db: Session = Depends(get_db),
):
    return HeartbeatMonitorService.check_offline_assets(
        db=db,
    )