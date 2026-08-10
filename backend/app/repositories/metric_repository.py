from uuid import UUID
from datetime import datetime, timedelta

from sqlalchemy import desc, func
from sqlalchemy.orm import Session

from app.models.metric import Metric


class MetricRepository:

    @staticmethod
    def create(
        db: Session,
        metric: Metric,
    ) -> Metric:
        db.add(metric)
        db.commit()
        db.refresh(metric)
        return metric

    @staticmethod
    def get_average_usage(db: Session):

        cpu, memory, disk = (
            db.query(
                func.avg(Metric.cpu_usage),
                func.avg(Metric.memory_usage),
                func.avg(Metric.disk_usage),
            )
            .one()
        )

        return (
            round(cpu or 0, 2),
            round(memory or 0, 2),
            round(disk or 0, 2),
        )

    @staticmethod
    def get_by_asset(
        db: Session,
        asset_id: UUID,
        page: int,
        size: int,
        period: str | None = None,
    ):
        query = (
            db.query(Metric)
            .filter(Metric.asset_id == asset_id)
        )

        if period:
            now = datetime.utcnow()

            periods = {
                "1h": timedelta(hours=1),
                "24h": timedelta(hours=24),
                "7d": timedelta(days=7),
                "30d": timedelta(days=30),
            }

            if period in periods:
                query = query.filter(
                    Metric.created_at >= now - periods[period]
                )

        total = query.count()

        metrics = (
            query
            .order_by(desc(Metric.created_at))
            .offset((page - 1) * size)
            .limit(size)
            .all()
        )

        return metrics, total

    @staticmethod
    def get_latest_metrics(
        db: Session,
        limit: int = 20,
    ):
        return (
            db.query(Metric)
            .order_by(desc(Metric.created_at))
            .limit(limit)
            .all()
        )

    @staticmethod
    def get_latest_by_asset(
        db: Session,
        asset_id: UUID,
    ):
        return (
            db.query(Metric)
            .filter(
                Metric.asset_id == asset_id,
            )
            .order_by(
                Metric.created_at.desc()
            )
            .first()
        )