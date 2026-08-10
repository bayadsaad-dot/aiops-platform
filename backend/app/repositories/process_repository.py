from uuid import UUID

from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.models.process import Process


class ProcessRepository:

    @staticmethod
    def get_top_cpu(
        db: Session,
        asset_id: UUID,
        limit: int = 10,
    ):
        return (
            db.query(Process)
            .filter(
                Process.asset_id == asset_id,
                Process.is_running == True,
                Process.cpu_percent > 0,
                Process.name != "System Idle Process",

            )
            .order_by(desc(Process.cpu_percent))
            .limit(limit)
            .all()
        )
    @staticmethod
    def create(
        db: Session,
        process: Process,
    ) -> Process:
        db.add(process)
        db.commit()
        db.refresh(process)
        return process

    @staticmethod
    def create_many(
        db: Session,
        processes: list[Process],
    ):
        db.add_all(processes)
        db.commit()

    @staticmethod
    def delete_by_asset(
        db: Session,
        asset_id: UUID,
    ):
        (
            db.query(Process)
            .filter(Process.asset_id == asset_id)
            .delete()
        )
        db.commit()

    @staticmethod
    def get_by_asset(
        db: Session,
        asset_id: UUID,
        page: int,
        size: int,
    ):
        query = (
            db.query(Process)
            .filter(Process.asset_id == asset_id)
        )

        total = query.count()

        processes = (
            query.order_by(desc(Process.cpu_percent))
            .offset((page - 1) * size)
            .limit(size)
            .all()
        )

        return processes, total

    @staticmethod
    def get_latest(
        db: Session,
        limit: int = 100,
    ):
        return (
            db.query(Process)
            .order_by(desc(Process.created_at))
            .limit(limit)
            .all()
        )

    @staticmethod
    def get_top_memory(
         db: Session,
         asset_id: UUID,
         limit: int = 10,
    ):
        return (
            db.query(Process)
            .filter(
                Process.asset_id == asset_id,
                Process.is_running == True,
                Process.memory_percent > 0,
                Process.name != "System Idle Process",
           )
           .order_by(desc(Process.memory_percent))
           .limit(limit)
           .all()
        )