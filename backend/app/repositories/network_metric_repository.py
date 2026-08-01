from uuid import UUID

from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.models.network_metric import NetworkMetric


class NetworkMetricRepository:

    @staticmethod
    def create(
        db: Session,
        metric: NetworkMetric,
    ) -> NetworkMetric:
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
    ):
        query = (
            db.query(NetworkMetric)
            .filter(NetworkMetric.asset_id == asset_id)
        )

        total = query.count()

        metrics = (
            query.order_by(desc(NetworkMetric.created_at))
            .offset((page - 1) * size)
            .limit(size)
            .all()
        )

        return metrics, total

    @staticmethod
    def get_by_interface(
        db: Session,
        interface_id: UUID,
        page: int,
        size: int,
    ):
        query = (
            db.query(NetworkMetric)
            .filter(
                NetworkMetric.interface_id == interface_id
            )
        )

        total = query.count()

        metrics = (
            query.order_by(desc(NetworkMetric.created_at))
            .offset((page - 1) * size)
            .limit(size)
            .all()
        )

        return metrics, total