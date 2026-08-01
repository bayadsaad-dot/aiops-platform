from app.models.network_interface import NetworkInterface
from app.repositories.asset_repository import AssetRepository
from app.repositories.network_interface_repository import (
    NetworkInterfaceRepository,
)


class NetworkService:

    @staticmethod
    def sync_interfaces(db, data):

        asset = AssetRepository.get_by_hostname(
            db,
            data.hostname,
        )

        if not asset:
            raise ValueError("Asset not found.")

        for item in data.interfaces:

            interface = (
                NetworkInterfaceRepository.get_by_name(
                    db=db,
                    asset_id=asset.id,
                    interface_name=item.name,
                )
            )

            if interface:

                interface.is_up = item.is_up
                interface.link_speed = item.speed
                interface.mtu = item.mtu

                NetworkInterfaceRepository.update(
                    db,
                    interface,
                )

            else:

                interface = NetworkInterface(
                    asset_id=asset.id,
                    interface_name=item.name,
                    interface_type="Unknown",
                    ipv4_address=None,
                    mac_address=None,
                    link_speed=item.speed,
                    mtu=item.mtu,
                    is_up=item.is_up,
                )

                NetworkInterfaceRepository.create(
                    db,
                    interface,
                )

        return {"message": "Interfaces synchronized successfully."}