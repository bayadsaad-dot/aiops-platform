from uuid import UUID
from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session

from app.models.metric import Metric
from app.schemas.metric import MetricCreate
from app.schemas.asset_summary import AssetSummary

from app.services.alert_engine import AlertEngine

from app.repositories.asset_repository import AssetRepository
from app.repositories.metric_repository import MetricRepository
from app.repositories.metric_stats_repository import MetricStatsRepository


class MetricService:

    @staticmethod
    def create_metric(
        db: Session,
        metric_data: MetricCreate,
    ):

        # Find Asset
        asset = AssetRepository.get_by_hostname(
            db,
            metric_data.hostname,
        )

        if not asset:
            asset = AssetRepository.get_by_ip(
                db,
                metric_data.ip_address,
            )

        if not asset:
            raise ValueError(
                f"No asset found for hostname '{metric_data.hostname}' "
                f"or IP '{metric_data.ip_address}'"
            )

        # Create Metric object
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

        # Save metric
        metric = MetricRepository.create(
            db,
            metric,
        )

        # Evaluate alerts
        AlertEngine.evaluate_metric(
            db=db,
            asset=asset,
            metric=metric,
        )

        return metric

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

    @staticmethod
    def get_asset_summary(
        db: Session,
        asset_id: UUID,
    ) -> AssetSummary:

        latest = MetricStatsRepository.get_latest_metric(
            db=db,
            asset_id=asset_id,
        )

        if latest is None:
            return AssetSummary(
                online=False,
                last_seen=None,
                current_cpu=None,
                avg_cpu_24h=None,
                max_cpu_24h=None,
                min_cpu_24h=None,
                current_memory=None,
                avg_memory_24h=None,
                current_disk=None,
                alerts=0,
            )

        avg_cpu, max_cpu, min_cpu = (
            MetricStatsRepository.get_cpu_stats_24h(
                db=db,
                asset_id=asset_id,
            )
        )

        avg_memory = (
            MetricStatsRepository.get_memory_avg_24h(
                db=db,
                asset_id=asset_id,
            )
        )

        now = datetime.now(timezone.utc)

        online = (
            now - latest.created_at
        ) < timedelta(minutes=2)

        return AssetSummary(
            online=online,
            last_seen=latest.created_at,
            current_cpu=latest.cpu_usage,
            avg_cpu_24h=avg_cpu,
            max_cpu_24h=max_cpu,
            min_cpu_24h=min_cpu,
            current_memory=latest.memory_usage,
            avg_memory_24h=avg_memory,
            current_disk=latest.disk_usage,
            alerts=0,
        )