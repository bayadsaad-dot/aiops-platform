from uuid import UUID

from sqlalchemy.orm import Session

from app.models.ai_analysis import AIAnalysis


class AIAnalysisRepository:

    @staticmethod
    def create(
        db: Session,
        analysis: AIAnalysis,
    ) -> AIAnalysis:
        db.add(analysis)
        db.commit()
        db.refresh(analysis)
        return analysis

    @staticmethod
    def update(
        db: Session,
        analysis: AIAnalysis,
    ) -> AIAnalysis:
        db.commit()
        db.refresh(analysis)
        return analysis

    @staticmethod
    def get_by_incident(
        db: Session,
        incident_id: UUID,
    ):
        return (
            db.query(AIAnalysis)
            .filter(
                AIAnalysis.incident_id == incident_id
            )
            .first()
        )

    @staticmethod
    def delete(
        db: Session,
        analysis: AIAnalysis,
    ):
        db.delete(analysis)
        db.commit()