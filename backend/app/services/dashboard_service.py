from app.repositories.asset_repository import AssetRepository
from app.repositories.alert_repository import AlertRepository
from app.repositories.metric_repository import MetricRepository

from app.schemas.dashboard import DashboardOverview


class DashboardService:

    @staticmethod
    def get_overview(db):

        total_assets = AssetRepository.count(db)

        online_assets = AssetRepository.count_online(db)
        offline_assets = total_assets - online_assets

        open_alerts = AlertRepository.count_open(db)

        avg_cpu, avg_memory, avg_disk = (
            MetricRepository.get_average_usage(db)
        )

        return DashboardOverview(
            total_assets=total_assets,
            online_assets=online_assets,
            offline_assets=offline_assets,
            open_alerts=open_alerts,
            avg_cpu=avg_cpu,
            avg_memory=avg_memory,
            avg_disk=avg_disk,
        )