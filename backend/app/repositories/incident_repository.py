from uuid import UUID

from sqlalchemy.orm import Session

from app.models.incident import Incident
from app.enums.incident import IncidentStatus


class IncidentRepository:

    @staticmethod
    def create(
        db: Session,
        incident: Incident,
    ) -> Incident:
        db.add(incident)
        db.commit()
        db.refresh(incident)
        return incident

    @staticmethod
    def update(
        db: Session,
        incident: Incident,
    ) -> Incident:
        db.commit()
        db.refresh(incident)
        return incident

    @staticmethod
    def get_by_id(
        db: Session,
        incident_id: UUID,
    ):
        return (
            db.query(Incident)
            .filter(Incident.id == incident_id)
            .first()
        )

    @staticmethod
    def get_all(
        db: Session,
        page: int,
        size: int,
    ):
        query = (
            db.query(Incident)
            .order_by(Incident.created_at.desc())
        )

        total = query.count()

        incidents = (
            query
            .offset((page - 1) * size)
            .limit(size)
            .all()
        )

        return incidents, total

    @staticmethod
    def get_open_by_alert(
        db: Session,
        alert_id: UUID,
    ):
        return (
            db.query(Incident)
            .filter(
                Incident.alert_id == alert_id,
                Incident.status != IncidentStatus.RESOLVED,
            )
            .first()
        )