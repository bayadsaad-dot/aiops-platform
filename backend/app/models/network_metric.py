from uuid import UUID

from sqlalchemy import (
    Float,
    BigInteger,
    ForeignKey,
    Index,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.models.base_model import BaseEntity


class NetworkMetric(BaseEntity):
    __tablename__ = "network_metrics"

    asset_id: Mapped[UUID] = mapped_column(
        ForeignKey("assets.id"),
        nullable=False,
    )

    interface_id: Mapped[UUID] = mapped_column(
        ForeignKey("network_interfaces.id"),
        nullable=False,
    )

    bytes_sent: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    bytes_received: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    packets_sent: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    packets_received: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    upload_speed: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    download_speed: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    asset = relationship(
        "Asset",
        back_populates="network_metrics",
    )

    interface = relationship(
        "NetworkInterface",
        back_populates="metrics",
    )

    __table_args__ = (
        Index("idx_network_metric_asset", "asset_id"),
        Index("idx_network_metric_interface", "interface_id"),
        Index("idx_network_metric_created", "created_at"),
    )