from pydantic import BaseModel


class DashboardOverview(BaseModel):

    total_assets: int

    online_assets: int
    offline_assets: int

    open_alerts: int

    avg_cpu: float
    avg_memory: float
    avg_disk: float