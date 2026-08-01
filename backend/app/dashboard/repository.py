from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session

from app.models.asset import Asset
from app.models.metric import Metric


class DashboardRepository:

    @staticmethod
    def get_summary(db: Session):

        total_assets = db.query(Asset).count()

        last_limit = datetime.now(timezone.utc) - timedelta(minutes=2)

        online_assets = (
            db.query(Metric.asset_id)
            .filter(Metric.created_at >= last_limit)
            .distinct()
            .count()
        )

        offline_assets = max(
            total_assets - online_assets,
            0,
        )

        active_alerts = 0

        return {
            "total_assets": total_assets,
            "online_assets": online_assets,
            "offline_assets": offline_assets,
            "active_alerts": active_alerts,
        }