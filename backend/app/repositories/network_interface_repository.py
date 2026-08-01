from uuid import UUID

from sqlalchemy.orm import Session

from app.models.network_interface import NetworkInterface


class NetworkInterfaceRepository:

    @staticmethod
    def get_by_asset(db: Session, asset_id: UUID):
        return (
            db.query(NetworkInterface)
            .filter(NetworkInterface.asset_id == asset_id)
            .all()
        )

    @staticmethod
    def get_by_name(
        db: Session,
        asset_id: UUID,
        interface_name: str,
    ):
        return (
            db.query(NetworkInterface)
            .filter(
                NetworkInterface.asset_id == asset_id,
                NetworkInterface.interface_name == interface_name,
            )
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        interface: NetworkInterface,
    ):
        db.add(interface)
        db.commit()
        db.refresh(interface)
        return interface

    @staticmethod
    def update(
        db: Session,
        interface: NetworkInterface,
    ):
        db.commit()
        db.refresh(interface)
        return interface