from app.models.network_metric import NetworkMetric

from app.repositories.asset_repository import AssetRepository
from app.repositories.network_interface_repository import (
    NetworkInterfaceRepository,
)
from app.repositories.network_metric_repository import (
    NetworkMetricRepository,
)


class NetworkMetricService:

    @staticmethod
    def create_metric(db, data):

        # Find Asset
        asset = AssetRepository.get_by_hostname(
            db,
            data.hostname,
        )

        if not asset:
            raise ValueError("Asset not found.")

        # Find Interface
        interface = (
            NetworkInterfaceRepository.get_by_name(
                db=db,
                asset_id=asset.id,
                interface_name=data.interface_name,
            )
        )

        if not interface:
            raise ValueError("Network interface not found.")

        metric = NetworkMetric(
            asset_id=asset.id,
            interface_id=interface.id,
            bytes_sent=data.bytes_sent,
            bytes_received=data.bytes_received,
            packets_sent=data.packets_sent,
            packets_received=data.packets_received,
            upload_speed=data.upload_speed,
            download_speed=data.download_speed,
        )

        return NetworkMetricRepository.create(
            db,
            metric,
        )

    @staticmethod
    def get_asset_metrics(
        db,
        asset_id,
        page,
        size,
    ):
        return NetworkMetricRepository.get_by_asset(
            db,
            asset_id,
            page,
            size,
        )