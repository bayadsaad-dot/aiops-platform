from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.deps import get_db
from app.schemas.heartbeat import HeartbeatRequest
from app.services.heartbeat_service import HeartbeatService

router = APIRouter(
    prefix="/api/v1/heartbeat",
    tags=["Heartbeat"],
)


@router.post("/")
def heartbeat(
    data: HeartbeatRequest,
    db: Session = Depends(get_db),
):
    return HeartbeatService.heartbeat(db, data)