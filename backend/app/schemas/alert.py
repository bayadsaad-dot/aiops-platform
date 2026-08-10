from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.enums.alert import AlertSeverity, AlertStatus


class AlertRead(BaseModel):

    id: UUID

    asset_id: UUID
    asset_hostname: str

    title: str
    message: str

    severity: AlertSeverity
    status: AlertStatus

    created_at: datetime
    resolved_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


class AlertListResponse(BaseModel):

    items: list[AlertRead]

    total: int
    page: int
    size: int