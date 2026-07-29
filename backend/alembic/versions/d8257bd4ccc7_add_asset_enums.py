"""add asset enums

Revision ID: d8257bd4ccc7
Revises: f0681ea9019e
Create Date: 2026-07-29 18:09:42.925759
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d8257bd4ccc7"
down_revision: Union[str, Sequence[str], None] = "f0681ea9019e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    asset_type_enum = sa.Enum(
        "PC",
        "Server",
        "Switch",
        "Router",
        "Firewall",
        "Printer",
        name="assettype",
    )

    asset_status_enum = sa.Enum(
        "Online",
        "Offline",
        "Maintenance",
        "Unknown",
        name="assetstatus",
    )

    # Create PostgreSQL enum types
    asset_type_enum.create(op.get_bind(), checkfirst=True)
    asset_status_enum.create(op.get_bind(), checkfirst=True)

    # Convert existing columns
    op.alter_column(
        "assets",
        "asset_type",
        existing_type=sa.VARCHAR(length=50),
        type_=asset_type_enum,
        postgresql_using="asset_type::assettype",
        existing_nullable=False,
    )

    op.alter_column(
        "assets",
        "status",
        existing_type=sa.VARCHAR(length=30),
        type_=asset_status_enum,
        postgresql_using="status::assetstatus",
        existing_nullable=False,
    )


def downgrade() -> None:
    """Downgrade schema."""

    asset_type_enum = sa.Enum(
        "PC",
        "Server",
        "Switch",
        "Router",
        "Firewall",
        "Printer",
        name="assettype",
    )

    asset_status_enum = sa.Enum(
        "Online",
        "Offline",
        "Maintenance",
        "Unknown",
        name="assetstatus",
    )

    op.alter_column(
        "assets",
        "status",
        existing_type=asset_status_enum,
        type_=sa.VARCHAR(length=30),
        postgresql_using="status::text",
        existing_nullable=False,
    )

    op.alter_column(
        "assets",
        "asset_type",
        existing_type=asset_type_enum,
        type_=sa.VARCHAR(length=50),
        postgresql_using="asset_type::text",
        existing_nullable=False,
    )

    asset_status_enum.drop(op.get_bind(), checkfirst=True)
    asset_type_enum.drop(op.get_bind(), checkfirst=True)