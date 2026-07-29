from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.enums.asset import AssetType, AssetStatus


class AssetCreate(BaseModel):
    hostname: str
    ip_address: str
    asset_type: AssetType
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
    asset_type: AssetType
    status: AssetStatus
    last_seen: datetime | None


class AssetListResponse(BaseModel):
    items: list[AssetResponse]
    total: int
    page: int
    size: int
    pages: int


class AssetUpdate(BaseModel):
    hostname: str
    ip_address: str
    asset_type: AssetType
    operating_system: str | None = None
    manufacturer: str | None = None
    model: str | None = None
    serial_number: str | None = None
    location: str | None = None