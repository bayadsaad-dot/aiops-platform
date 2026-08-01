from pydantic import BaseModel


class InterfaceCreate(BaseModel):
    name: str
    is_up: bool
    speed: int
    mtu: int


class NetworkSyncRequest(BaseModel):
    hostname: str
    ip_address: str

    bytes_sent: int
    bytes_received: int

    packets_sent: int
    packets_received: int

    interfaces: list[InterfaceCreate]