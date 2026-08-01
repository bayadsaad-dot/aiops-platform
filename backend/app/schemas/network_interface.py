from uuid import UUID
from datetime import datetime

from pydantic import BaseModel


class NetworkInterfaceResponse(BaseModel):
    id: UUID

    interface_name: str

    interface_type: str

    ipv4_address: str | None

    mac_address: str | None

    link_speed: int

    mtu: int

    is_up: bool

    last_seen: datetime

    class Config:
        from_attributes = True