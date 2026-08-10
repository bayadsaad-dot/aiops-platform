from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class WebsiteCreate(BaseModel):
    name: str
    url: str


class WebsiteRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    url: str

    status: str
    status_code: int | None = None
    response_time: float | None = None

    ssl_expiry: datetime | None = None
    last_check: datetime | None = None

    created_at: datetime
    updated_at: datetime