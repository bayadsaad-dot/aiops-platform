from sqlalchemy.orm import Session

from app.dashboard.repository import DashboardRepository


class DashboardService:

    @staticmethod
    def get_summary(db: Session):
        return DashboardRepository.get_summary(db)