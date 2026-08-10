from datetime import datetime, timezone

from app.enums.asset import AssetStatus
from app.repositories.asset_repository import AssetRepository
from app.services.alert_service import AlertService


class HeartbeatService:

    @staticmethod
    def heartbeat(db, data):

        asset = AssetRepository.get_by_hostname(
            db,
            data.hostname,
        )

        if not asset:
            raise ValueError("Asset not found.")

        print("\n========== HEARTBEAT ==========")
        print("Hostname:", asset.hostname)
        print("Current Status:", asset.status)

        if asset.status == AssetStatus.OFFLINE:
            print(">>> Resolving offline alert...")

            AlertService.resolve_offline_alert(
                db=db,
                asset=asset,
            )

        asset.last_seen = datetime.now(timezone.utc)
        asset.status = AssetStatus.ONLINE

        AssetRepository.update(db, asset)

        print("Updated Status:", asset.status)

        return asset