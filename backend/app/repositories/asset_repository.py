from uuid import UUID

from sqlalchemy.orm import Session

from app.models.asset import Asset


class AssetRepository:

    @staticmethod
    def create(db: Session, asset: Asset) -> Asset:
        db.add(asset)
        db.commit()
        db.refresh(asset)
        return asset

    @staticmethod
    def get_all(db: Session):
        return db.query(Asset).all()

    @staticmethod
    def get_by_id(db: Session, asset_id: UUID):
        return (
            db.query(Asset)
            .filter(Asset.id == asset_id)
            .first()
        )

    @staticmethod
    def get_by_hostname(db: Session, hostname: str):
        return (
            db.query(Asset)
            .filter(Asset.hostname == hostname)
            .first()
        )

    @staticmethod
    def get_by_ip(db: Session, ip: str):
        return (
            db.query(Asset)
            .filter(Asset.ip_address == ip)
            .first()
        )

    @staticmethod
    def delete(db: Session, asset: Asset):
        db.delete(asset)
        db.commit()