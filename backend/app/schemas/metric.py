from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class MetricCreate(BaseModel):
    hostname: str
    ip_address: str

    cpu_usage: float
    memory_usage: float
    disk_usage: float

    uptime_seconds: int
    boot_time: str
class MetricRead(BaseModel):
    id: UUID
    asset_id: UUID

    hostname: str
    ip_address: str

    cpu_usage: float
    memory_usage: float
    disk_usage: float

    uptime_seconds: int
    boot_time: datetime

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class MetricListResponse(BaseModel):
    items: list[MetricRead]
    total: int
    page: int
    size: int