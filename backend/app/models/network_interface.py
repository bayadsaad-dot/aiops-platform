from uuid import UUID
from datetime import datetime, timezone

from sqlalchemy import (
    String,
    Integer,
    Boolean,
    ForeignKey,
    DateTime,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.models.base_model import BaseEntity


class NetworkInterface(BaseEntity):
    __tablename__ = "network_interfaces"

    asset_id: Mapped[UUID] = mapped_column(
        ForeignKey("assets.id"),
        nullable=False,
    )

    interface_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    interface_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    ipv4_address: Mapped[str | None] = mapped_column(
        String(45),
        nullable=True,
    )

    mac_address: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    link_speed: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    mtu: Mapped[int] = mapped_column(
        Integer,
        default=1500,
    )

    is_up: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    last_seen: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    asset = relationship(
        "Asset",
        back_populates="network_interfaces",
    )

    metrics = relationship(
        "NetworkMetric",
        back_populates="interface",
        cascade="all, delete-orphan",
    )