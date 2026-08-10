from sqlalchemy.orm import Session

from app.models.alert import Alert
from app.enums.alert import AlertStatus


class AlertRepository:

    @staticmethod
    def get_open_alert(
        db: Session,
        asset_id,
        title: str,
    ):
        return (
            db.query(Alert)
            .filter(
                Alert.asset_id == asset_id,
                Alert.title == title,
                Alert.status == AlertStatus.OPEN,
            )
            .first()
        )

    @staticmethod
    def get_all(
        db: Session,
        page: int,
        size: int,
    ):
        query = db.query(Alert).order_by(Alert.created_at.desc())

        total = query.count()

        alerts = (
            query.offset((page - 1) * size)
            .limit(size)
            .all()
        )

        return alerts, total

    @staticmethod
    def get_open(
        db: Session,
    ):
        return (
            db.query(Alert)
            .filter(Alert.status == AlertStatus.OPEN)
            .order_by(Alert.created_at.desc())
            .all()
        )

    @staticmethod
    def count_open(
        db: Session,
    ):
        return (
            db.query(Alert)
            .filter(Alert.status == AlertStatus.OPEN)
            .count()
        )

    @staticmethod
    def create(
        db: Session,
        alert: Alert,
    ) -> Alert:
        db.add(alert)
        db.commit()
        db.refresh(alert)
        return alert

    @staticmethod
    def update(
        db: Session,
        alert: Alert,
    ):
        db.commit()
        db.refresh(alert)
        return alert