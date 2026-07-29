from uuid import UUID
from sqlalchemy import desc
from sqlalchemy.orm import Session
from sqlalchemy import desc, or_, func
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
    def get_assets(
        db: Session,
        page: int,
        size: int,
        search: str | None = None,
        asset_type=None,
        status=None,
    ):
        query = db.query(Asset)

        if search:
            query = query.filter(
                or_(
                    Asset.hostname.ilike(f"%{search}%"),
                    Asset.asset_code.ilike(f"%{search}%"),
                    Asset.ip_address.ilike(f"%{search}%"),
                )
            )

        if asset_type:
              query = query.filter(Asset.asset_type == asset_type)

        if status:
             query = query.filter(Asset.status == status)

        total = query.with_entities(func.count()).scalar()

        assets = (
            query.order_by(desc(Asset.created_at))
            .offset((page - 1) * size)
            .limit(size)
            .all()
        )

        return assets, total

    
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
    def get_last_asset_by_type(db: Session, asset_type: str):
        return (
            db.query(Asset)
            .filter(Asset.asset_type == asset_type)
            .order_by(desc(Asset.asset_code))
            .first()
        )

    @staticmethod
    def delete(db: Session, asset: Asset):
        db.delete(asset)
        db.commit()

    @staticmethod
    def update(db: Session, asset: Asset):
        db.commit()
        db.refresh(asset)
        return asset