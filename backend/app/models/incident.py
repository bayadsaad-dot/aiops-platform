from uuid import UUID

from sqlalchemy import String, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseEntity
from app.enums.incident import IncidentPriority, IncidentStatus


class Incident(BaseEntity):
    __tablename__ = "incidents"

    asset_id: Mapped[UUID] = mapped_column(
        ForeignKey("assets.id"),
        nullable=False,
    )

    alert_id: Mapped[UUID] = mapped_column(
        ForeignKey("alerts.id"),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        String(1000),
        nullable=False,
    )

    priority: Mapped[IncidentPriority] = mapped_column(
        Enum(IncidentPriority),
        nullable=False,
    )

    status: Mapped[IncidentStatus] = mapped_column(
        Enum(IncidentStatus),
        default=IncidentStatus.OPEN,
        nullable=False,
    )

    assigned_to: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    asset = relationship(
        "Asset",
        back_populates="incidents",
    )

    alert = relationship(
        "Alert",
        back_populates="incident",
    )