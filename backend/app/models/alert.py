from uuid import UUID

from sqlalchemy import String, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseEntity
from app.enums.alert import AlertSeverity, AlertStatus
from datetime import datetime
from sqlalchemy import DateTime

class Alert(BaseEntity):
    __tablename__ = "alerts"

    asset_id: Mapped[UUID] = mapped_column(
        ForeignKey("assets.id"),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    message: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    severity: Mapped[AlertSeverity] = mapped_column(
        Enum(AlertSeverity),
        nullable=False,
    )

    status: Mapped[AlertStatus] = mapped_column(
        Enum(AlertStatus),
        default=AlertStatus.OPEN,
        nullable=False,
    )

    resolved_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    asset = relationship(
        "Asset",
        back_populates="alerts",
    )

    @property
    def asset_hostname(self):
        return self.asset.hostname if self.asset else ""

    incident = relationship(
       "Incident",
        uselist=False,
        back_populates="alert",
    )