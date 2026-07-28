from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class AssetCreate(BaseModel):
    hostname: str
    ip_address: str
    asset_type: str
    operating_system: str | None = None
    manufacturer: str | None = None
    model: str | None = None
    serial_number: str | None = None
    location: str | None = None


class AssetResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    asset_code: str
    hostname: str
    ip_address: str
    asset_type: str
    status: str
    last_seen: datetime | None