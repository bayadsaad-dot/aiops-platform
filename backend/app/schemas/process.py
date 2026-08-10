from uuid import UUID
from datetime import datetime

from pydantic import BaseModel


class ProcessCreate(BaseModel):
    pid: int
    name: str
    cpu_percent: float
    memory_percent: float
    executable: str | None = None
    username: str | None = None
    is_running: bool = True


class ProcessRead(BaseModel):
    id: UUID
    asset_id: UUID
    pid: int
    name: str
    cpu_percent: float
    memory_percent: float
    executable: str | None
    username: str | None
    is_running: bool
    created_at: datetime

    model_config = {
        "from_attributes": True,
    }


class ProcessListResponse(BaseModel):
    items: list[ProcessRead]
    total: int
    page: int
    size: int