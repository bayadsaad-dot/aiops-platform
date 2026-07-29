from app.models.asset import Asset
from app.repositories.asset_repository import AssetRepository
from app.utils.asset_code_generator import generate_asset_code


class AssetService:

    @staticmethod
    def get_asset_by_id(db, asset_id):
        asset = AssetRepository.get_by_id(db, asset_id)

        if not asset:
            raise ValueError("Asset not found.")

        return asset

    @staticmethod
    def delete_asset(db, asset_id):
         asset = AssetRepository.get_by_id(db, asset_id)

         if not asset:
             raise ValueError("Asset not found.")

         AssetRepository.delete(db, asset)
    
    @staticmethod
    def get_all_assets(db):
        return AssetRepository.get_all(db)

    @staticmethod
    def get_assets(
        db,
        page,
        size,
        search=None,
        asset_type=None,
        status=None,
   ):
        return AssetRepository.get_assets(
            db=db,
            page=page,
            size=size,
            search=search,
            asset_type=asset_type,
            status=status,
        )
    
    @staticmethod
    def update_asset(db, asset_id, data):
       asset = AssetRepository.get_by_id(db, asset_id)

       if not asset:
         raise ValueError("Asset not found.")

       asset.hostname = data.hostname
       asset.ip_address = data.ip_address
       asset.asset_type = data.asset_type
       asset.operating_system = data.operating_system
       asset.manufacturer = data.manufacturer
       asset.model = data.model
       asset.serial_number = data.serial_number
       asset.location = data.location

       return AssetRepository.update(db, asset)

    @staticmethod
    def create_asset(db, data):
        # Check duplicate hostname
        if AssetRepository.get_by_hostname(db, data.hostname):
            raise ValueError("Hostname already exists.")

        # Check duplicate IP
        if AssetRepository.get_by_ip(db, data.ip_address):
            raise ValueError("IP address already exists.")

        # Generate asset code
        last_asset = AssetRepository.get_last_asset_by_type(
            db,
            data.asset_type
        )

        asset_code = generate_asset_code(
            last_asset=last_asset,
            asset_type=data.asset_type,
        )

        # Create asset
        asset = Asset(
            asset_code=asset_code,
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