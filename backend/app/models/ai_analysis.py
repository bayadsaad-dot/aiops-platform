from uuid import UUID

from sqlalchemy import (
    Text,
    Integer,
    ForeignKey,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.models.base_model import BaseEntity


class AIAnalysis(BaseEntity):
    __tablename__ = "ai_analysis"

    incident_id: Mapped[UUID] = mapped_column(
        ForeignKey("incidents.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )

    summary: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    root_cause: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    impact: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    confidence: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    recommendations: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    incident = relationship("Incident")