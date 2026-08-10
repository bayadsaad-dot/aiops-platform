from app.repositories.metric_repository import MetricRepository
from app.schemas.dashboard_metrics import (
    DashboardMetrics,
    MetricPoint,
)


class DashboardMetricsService:

    @staticmethod
    def get_metrics(db):

        metrics = MetricRepository.get_latest_metrics(db)

        metrics.reverse()

        return DashboardMetrics(
            cpu=[
                MetricPoint(
                    time=m.created_at,
                    value=m.cpu_usage,
                )
                for m in metrics
            ],
            memory=[
                MetricPoint(
                    time=m.created_at,
                    value=m.memory_usage,
                )
                for m in metrics
            ],
            disk=[
                MetricPoint(
                    time=m.created_at,
                    value=m.disk_usage,
                )
                for m in metrics
            ],
        )