from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.alert import Alert
from app.repositories.alert_repository import AlertRepository
from app.enums.alert import AlertSeverity, AlertStatus


class AlertService:

    @staticmethod
    def get_alerts(
        db: Session,
        page: int,
        size: int,
    ):
        return AlertRepository.get_all(
            db=db,
            page=page,
            size=size,
        )

    @staticmethod
    def get_open_alerts(
        db: Session,
    ):
        return AlertRepository.get_open(
            db=db,
        )

    @staticmethod
    def create_offline_alert(
        db: Session,
        asset,
    ):
        existing = AlertRepository.get_open_alert(
            db=db,
            asset_id=asset.id,
            title="Asset Offline",
        )

        if existing:
            return existing

        alert = Alert(
            asset_id=asset.id,
            severity=AlertSeverity.CRITICAL,
            status=AlertStatus.OPEN,
            title="Asset Offline",
            message=f"{asset.hostname} heartbeat timeout.",
        )

        return AlertRepository.create(
            db=db,
            alert=alert,
        )

    @staticmethod
    def resolve_offline_alert(
        db: Session,
        asset,
    ):
        alert = AlertRepository.get_open_alert(
            db=db,
            asset_id=asset.id,
            title="Asset Offline",
        )

        if not alert:
            return None

        alert.status = AlertStatus.RESOLVED
        alert.resolved_at = datetime.now(timezone.utc)

        return AlertRepository.update(
            db=db,
            alert=alert,
        )