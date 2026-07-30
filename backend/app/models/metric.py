from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseEntity
from sqlalchemy import Index

class Metric(BaseEntity):
    __tablename__ = "metrics"
    asset_id: Mapped[str] = mapped_column(
        ForeignKey("assets.id"),
        nullable=False,
    )


    hostname: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    ip_address: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
    )

    cpu_usage: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    memory_usage: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    disk_usage: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    uptime_seconds: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    boot_time: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    asset = relationship(
         "Asset",
         back_populates="metrics",
    )
    __table_args__ = (
        Index("idx_metric_asset_id", "asset_id"),
        Index("idx_metric_created_at", "created_at"),
        Index("idx_metric_asset_created", "asset_id", "created_at"),
   )