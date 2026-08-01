from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class NetworkMetricCreate(BaseModel):
    hostname: str
    interface_name: str

    bytes_sent: int
    bytes_received: int

    packets_sent: int
    packets_received: int

    upload_speed: float
    download_speed: float


class NetworkMetricRead(BaseModel):
    id: UUID

    asset_id: UUID
    interface_id: UUID

    bytes_sent: int
    bytes_received: int

    packets_sent: int
    packets_received: int

    upload_speed: float
    download_speed: float

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class NetworkMetricListResponse(BaseModel):
    items: list[NetworkMetricRead]

    total: int
    page: int
    size: int