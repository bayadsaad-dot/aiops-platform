from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.enums.incident import (
    IncidentPriority,
    IncidentStatus,
)


class IncidentRead(BaseModel):

    id: UUID

    asset_id: UUID
    alert_id: UUID

    title: str
    description: str

    priority: IncidentPriority
    status: IncidentStatus

    assigned_to: str | None = None

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )


class IncidentListResponse(BaseModel):

    items: list[IncidentRead]

    total: int
    page: int
    size: int