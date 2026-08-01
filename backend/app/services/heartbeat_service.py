from datetime import datetime, timezone

from app.enums.asset import AssetStatus
from app.repositories.asset_repository import AssetRepository


class HeartbeatService:

    @staticmethod
    def heartbeat(db, data):

        asset = AssetRepository.get_by_hostname(
            db,
            data.hostname,
        )

        if not asset:
            raise ValueError("Asset not found.")

        asset.last_seen = datetime.now(timezone.utc)
        asset.status = AssetStatus.ONLINE

        return AssetRepository.update(db, asset)