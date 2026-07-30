"""add metric indexes

Revision ID: 206692ab8cb8
Revises: 892123732022
Create Date: 2026-07-30 17:31:39.888601
"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "206692ab8cb8"
down_revision: Union[str, Sequence[str], None] = "892123732022"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_index(
        "idx_metric_asset_created",
        "metrics",
        ["asset_id", "created_at"],
        unique=False,
    )

    op.create_index(
        "idx_metric_asset_id",
        "metrics",
        ["asset_id"],
        unique=False,
    )

    op.create_index(
        "idx_metric_created_at",
        "metrics",
        ["created_at"],
        unique=False,
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_index(
        "idx_metric_created_at",
        table_name="metrics",
    )

    op.drop_index(
        "idx_metric_asset_id",
        table_name="metrics",
    )

    op.drop_index(
        "idx_metric_asset_created",
        table_name="metrics",
    )