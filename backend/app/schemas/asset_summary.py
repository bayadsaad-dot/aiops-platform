from datetime import datetime

from pydantic import BaseModel


class AssetSummary(BaseModel):
    online: bool
    last_seen: datetime | None

    current_cpu: float | None
    avg_cpu_24h: float | None
    max_cpu_24h: float | None
    min_cpu_24h: float | None

    current_memory: float | None
    avg_memory_24h: float | None

    current_disk: float | None

    alerts: int