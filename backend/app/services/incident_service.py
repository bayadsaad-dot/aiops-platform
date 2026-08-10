from sqlalchemy.orm import Session

from app.models.incident import Incident

from app.enums.incident import (
    IncidentPriority,
    IncidentStatus,
)

from app.repositories.incident_repository import (
    IncidentRepository,
)


class IncidentService:

    @staticmethod
    def get_incidents(
        db: Session,
        page: int,
        size: int,
    ):
        return IncidentRepository.get_all(
            db=db,
            page=page,
            size=size,
        )

    @staticmethod
    def create_from_alert(
        db: Session,
        alert,
    ):

        existing = IncidentRepository.get_open_by_alert(
            db=db,
            alert_id=alert.id,
        )

        if existing:
            return existing

        incident = Incident(
            asset_id=alert.asset_id,
            alert_id=alert.id,
            title=alert.title,
            description=alert.message,
            priority=IncidentPriority.CRITICAL,
            status=IncidentStatus.OPEN,
        )

        return IncidentRepository.create(
            db=db,
            incident=incident,
        )

    @staticmethod
    def resolve(
        db: Session,
        incident: Incident,
    ):
        incident.status = IncidentStatus.RESOLVED

        return IncidentRepository.update(
            db=db,
            incident=incident,
        )

    @staticmethod
    def assign(
        db: Session,
        incident: Incident,
        analyst: str,
    ):
        incident.assigned_to = analyst
        incident.status = IncidentStatus.IN_PROGRESS

        return IncidentRepository.update(
            db=db,
            incident=incident,
        )