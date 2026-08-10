from uuid import UUID

from sqlalchemy import (
    String,
    Integer,
    Float,
    Boolean,
    ForeignKey,
    Index,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.models.base_model import BaseEntity


class Process(BaseEntity):
    __tablename__ = "processes"

    asset_id: Mapped[UUID] = mapped_column(
        ForeignKey("assets.id"),
        nullable=False,
    )

    pid: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    cpu_percent: Mapped[float] = mapped_column(
        Float,
        default=0,
    )

    memory_percent: Mapped[float] = mapped_column(
        Float,
        default=0,
    )

    executable: Mapped[str] = mapped_column(
        String(500),
        nullable=True,
    )

    username: Mapped[str] = mapped_column(
        String(255),
        nullable=True,
    )

    is_running: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    asset = relationship(
        "Asset",
        back_populates="processes",
    )

    __table_args__ = (
        Index("idx_process_asset", "asset_id"),
        Index("idx_process_name", "name"),
        Index("idx_process_pid", "pid"),
    )