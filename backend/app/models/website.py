from sqlalchemy import (
    String,
    Integer,
    Float,
    DateTime,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from app.models.base_model import BaseEntity


class Website(BaseEntity):
    __tablename__ = "websites"

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    url: Mapped[str] = mapped_column(
        String(500),
        unique=True,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="UNKNOWN",
    )

    status_code: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    response_time: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    ssl_expiry: Mapped[DateTime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    last_check: Mapped[DateTime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )