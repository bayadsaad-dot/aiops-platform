from datetime import datetime, timezone

import requests
from sqlalchemy.orm import Session

from app.models.website import Website
from app.repositories.website_repository import WebsiteRepository


class WebsiteService:

    @staticmethod
    def get_websites(
        db: Session,
    ):
        return WebsiteRepository.get_all(db)

    @staticmethod
    def create_website(
        db: Session,
        name: str,
        url: str,
    ):
        existing = WebsiteRepository.get_by_url(
            db=db,
            url=url,
        )

        if existing:
            raise ValueError("Website already exists.")

        website = Website(
            name=name,
            url=url,
            status="UNKNOWN",
        )

        return WebsiteRepository.create(
            db=db,
            website=website,
        )

    @staticmethod
    def delete_website(
        db: Session,
        website_id,
    ):
        website = WebsiteRepository.get_by_id(
            db=db,
            website_id=website_id,
        )

        if not website:
            raise ValueError("Website not found.")

        WebsiteRepository.delete(
            db=db,
            website=website,
        )

        return {
            "message": "Website deleted successfully."
        }

    @staticmethod
    def check_website(
        db: Session,
        website: Website,
    ):
        try:
            response = requests.get(
                website.url,
                timeout=5,
            )

            website.status = "UP"
            website.status_code = response.status_code
            website.response_time = (
                response.elapsed.total_seconds() * 1000
            )

        except Exception:
            website.status = "DOWN"
            website.status_code = None
            website.response_time = None

        website.last_check = datetime.now(
            timezone.utc
        )

        return WebsiteRepository.update(
            db=db,
            website=website,
        )

    @staticmethod
    def check_all_websites(
        db: Session,
    ):
        websites = WebsiteRepository.get_all(db)

        for website in websites:
            WebsiteService.check_website(
                db=db,
                website=website,
            )

        return {
            "checked": len(websites),
        }