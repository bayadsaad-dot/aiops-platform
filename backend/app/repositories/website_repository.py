from sqlalchemy.orm import Session
from sqlalchemy import desc

from app.models.website import Website


class WebsiteRepository:

    @staticmethod
    def create(
        db: Session,
        website: Website,
    ) -> Website:
        db.add(website)
        db.commit()
        db.refresh(website)
        return website

    @staticmethod
    def get_all(
        db: Session,
    ):
        return (
            db.query(Website)
            .order_by(desc(Website.created_at))
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        website_id,
    ):
        return (
            db.query(Website)
            .filter(Website.id == website_id)
            .first()
        )

    @staticmethod
    def get_by_url(
        db: Session,
        url: str,
    ):
        return (
            db.query(Website)
            .filter(Website.url == url)
            .first()
        )

    @staticmethod
    def update(
        db: Session,
        website: Website,
    ):
        db.commit()
        db.refresh(website)
        return website

    @staticmethod
    def delete(
        db: Session,
        website: Website,
    ):
        db.delete(website)
        db.commit()