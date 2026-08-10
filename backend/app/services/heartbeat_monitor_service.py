from sqlalchemy.orm import Session
import asyncio

from app.enums.asset import AssetStatus
from app.repositories.asset_repository import AssetRepository
from app.services.alert_service import AlertService
from app.websocket.manager import manager


class HeartbeatMonitorService:

    @staticmethod
    def check_offline_assets(
        db: Session,
    ):
        expired_assets = (
            AssetRepository.get_expired_heartbeats(
                db=db,
                timeout_seconds=5,
            )
        )

        updated = 0

        for asset in expired_assets:

            if asset.status == AssetStatus.OFFLINE:
                continue

            asset.status = AssetStatus.OFFLINE

            AlertService.create_offline_alert(
                db=db,
                asset=asset,
            )

            print(f"Broadcasting offline alert for: {asset.hostname}")

            updated += 1

            try:
                asyncio.run(
                    manager.broadcast(
                        {
                            "type": "alert_created",
                            "asset": asset.hostname,
                        }
                    )
                )
            except Exception as e:
                print(f"Broadcast error: {e}")

        db.commit()

        return {
            "updated": updated,
        }