from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, Enum
from sqlalchemy.orm import relationship
from app.enums.asset import AssetType, AssetStatus
from app.models.base_model import BaseEntity


class Asset(BaseEntity):
    __tablename__ = "assets"

    asset_code: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    hostname: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    ip_address: Mapped[str] = mapped_column(
        String(45),
        unique=True,
        nullable=False,
    )

    asset_type: Mapped[AssetType] = mapped_column(
        Enum(
             AssetType,
             values_callable=lambda enum: [e.value for e in enum],
             name="assettype",
        ),
        nullable=False,
    )

    operating_system: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    manufacturer: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    model: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    serial_number: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    location: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    status: Mapped[AssetStatus] = mapped_column(
         Enum(
         AssetStatus,
         values_callable=lambda enum: [e.value for e in enum],
         name="assetstatus",
       ),
      default=AssetStatus.OFFLINE,
     nullable=False,
    )

    last_seen: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
    metrics = relationship(
        "Metric",
        back_populates="asset",
        cascade="all, delete-orphan",
    )

    network_interfaces = relationship(
         "NetworkInterface",
         back_populates="asset",
         cascade="all, delete-orphan",
    )

    network_metrics = relationship(
         "NetworkMetric",
          back_populates="asset",
          cascade="all, delete-orphan",
    )