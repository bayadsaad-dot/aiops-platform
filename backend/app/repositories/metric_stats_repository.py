from datetime import datetime, timedelta
from uuid import UUID

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.metric import Metric


class MetricStatsRepository:

    @staticmethod
    def get_latest_metric(
        db: Session,
        asset_id: UUID,
    ):
        return (
            db.query(Metric)
            .filter(Metric.asset_id == asset_id)
            .order_by(Metric.created_at.desc())
            .first()
        )

    @staticmethod
    def get_cpu_stats_24h(
        db: Session,
        asset_id: UUID,
    ):
        since = datetime.utcnow() - timedelta(hours=24)

        return (
            db.query(
                func.avg(Metric.cpu_usage),
                func.max(Metric.cpu_usage),
                func.min(Metric.cpu_usage),
            )
            .filter(
                Metric.asset_id == asset_id,
                Metric.created_at >= since,
            )
            .first()
        )

    @staticmethod
    def get_memory_avg_24h(
        db: Session,
        asset_id: UUID,
    ):
        since = datetime.utcnow() - timedelta(hours=24)

        return (
            db.query(
                func.avg(Metric.memory_usage),
            )
            .filter(
                Metric.asset_id == asset_id,
                Metric.created_at >= since,
            )
            .scalar()
        )