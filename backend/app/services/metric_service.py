from uuid import UUID

from sqlalchemy.orm import Session

from app.models.metric import Metric
from app.repositories.asset_repository import AssetRepository
from app.repositories.metric_repository import MetricRepository
from app.schemas.metric import MetricCreate


class MetricService:

    @staticmethod
    def create_metric(db: Session, metric_data: MetricCreate):

        asset = AssetRepository.get_by_hostname(db, metric_data.hostname)

        if not asset:
            asset = AssetRepository.get_by_ip(db, metric_data.ip_address)

        if not asset:
            raise ValueError(
                f"No asset found for hostname '{metric_data.hostname}' "
                f"or IP '{metric_data.ip_address}'"
            )

        metric = Metric(
            hostname=metric_data.hostname,
            ip_address=metric_data.ip_address,
            cpu_usage=metric_data.cpu_usage,
            memory_usage=metric_data.memory_usage,
            disk_usage=metric_data.disk_usage,
            uptime_seconds=metric_data.uptime_seconds,
            boot_time=metric_data.boot_time,
            asset_id=asset.id,
        )

        return MetricRepository.create(db, metric)

    @staticmethod
    def get_asset_metrics(
        db: Session,
        asset_id: UUID,
        page: int,
        size: int,
        period: str | None = None,
    ):
        return MetricRepository.get_by_asset(
            db=db,
            asset_id=asset_id,
            page=page,
            size=size,
            period=period,
        )