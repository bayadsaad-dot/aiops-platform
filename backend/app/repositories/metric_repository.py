from uuid import UUID

from sqlalchemy import desc
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.models.metric import Metric


class MetricRepository:

    @staticmethod
    def create(db: Session, metric: Metric) -> Metric:
        db.add(metric)
        db.commit()
        db.refresh(metric)
        return metric

    @staticmethod
    def get_by_asset(
        db: Session,
        asset_id: UUID,
        page: int,
        size: int,
        period: str | None = None,
    ):
        query = db.query(Metric).filter(
            
            Metric.asset_id == asset_id
        )
        if period:
            now = datetime.utcnow()

            periods = {
                "1h":  timedelta(hours=1),
                "24h": timedelta(hours=24),
                "7d":  timedelta(days=7),
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