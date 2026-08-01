from pydantic import BaseModel


class DashboardSummary(BaseModel):
    total_assets: int
    online_assets: int
    offline_assets: int
    active_alerts: int