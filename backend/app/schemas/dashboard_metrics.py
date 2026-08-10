from datetime import datetime
from pydantic import BaseModel


class MetricPoint(BaseModel):
    time: datetime
    value: float


class DashboardMetrics(BaseModel):
    cpu: list[MetricPoint]
    memory: list[MetricPoint]
    disk: list[MetricPoint]