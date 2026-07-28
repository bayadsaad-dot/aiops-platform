from app.models.asset import Asset
from app.repositories.asset_repository import AssetRepository


class AssetService:

    @staticmethod
    def create_asset(db, data):
        if AssetRepository.get_by_hostname(db, data.hostname):
            raise ValueError("Hostname already exists.")

        if AssetRepository.get_by_ip(db, data.ip_address):
            raise ValueError("IP address already exists.")

        asset = Asset(
            asset_code="TEMP",
            hostname=data.hostname,
            ip_address=data.ip_address,
            asset_type=data.asset_type,
            operating_system=data.operating_system,
            manufacturer=data.manufacturer,
            model=data.model,
            serial_number=data.serial_number,
            location=data.location,
        )

        return AssetRepository.create(db, asset)