from pydantic import BaseModel


class HeartbeatRequest(BaseModel):
    hostname: str