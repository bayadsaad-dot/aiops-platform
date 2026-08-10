from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session

from app.models.heartbeat import Heartbeat


class HeartbeatRepository:

    @staticmethod
    def count_online(db: Session):

        threshold = datetime.now(timezone.utc) - timedelta(minutes=2)

        return (
            db.query(Heartbeat)
            .filter(Heartbeat.last_seen >= threshold)
            .count()
        )