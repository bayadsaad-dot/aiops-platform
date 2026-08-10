from sqlalchemy.orm import Session

from app.models.process import Process
from app.schemas.process import ProcessCreate

from uuid import UUID
from app.repositories.asset_repository import AssetRepository
from app.repositories.process_repository import ProcessRepository


class ProcessService:

    @staticmethod
    def save_processes(
        db: Session,
        hostname: str,
        processes: list[ProcessCreate],
    ):
        asset = AssetRepository.get_by_hostname(
            db=db,
            hostname=hostname,
        )

        if not asset:
            raise ValueError("Asset not found.")

        # Delete previous snapshot
        ProcessRepository.delete_by_asset(
            db=db,
            asset_id=asset.id,
        )

        process_models = []

        for process in processes:

            process_models.append(
                Process(
                    asset_id=asset.id,
                    pid=process.pid,
                    name=process.name,
                    cpu_percent=process.cpu_percent,
                    memory_percent=process.memory_percent,
                    executable=process.executable,
                    username=process.username,
                    is_running=process.is_running,
                )
            )

        ProcessRepository.create_many(
            db=db,
            processes=process_models,
        )

        return {
            "saved": len(process_models),
        }

    @staticmethod
    def get_asset_processes(
        db: Session,
        asset_id: UUID,
        page: int,
        size: int,
    ):
        return ProcessRepository.get_by_asset(
            db=db,
            asset_id=asset_id,
            page=page,
            size=size,
        )

    @staticmethod 
    def get_top_cpu(
        db: Session,
        asset_id: UUID,
        limit: int = 10,

    ):
        return ProcessRepository.get_top_cpu(
            db=db,
            asset_id=asset_id,
            limit=limit,
    )

    @staticmethod
    def get_top_memory(
        db: Session,
        asset_id: UUID,
        limit: int = 10,
   ):
        return ProcessRepository.get_top_memory(
            db=db,
            asset_id=asset_id,
            limit=limit,
        )