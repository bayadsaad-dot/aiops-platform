from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
)

from sqlalchemy.orm import Session

from app.database.deps import get_db

from app.schemas.process import (
    ProcessCreate,
    ProcessListResponse,
)

from app.services.process_service import (
    ProcessService,
)

router = APIRouter(
    prefix="/api/v1/processes",
    tags=["Processes"],
)


@router.post(
    "/{hostname}",
)
def save_processes(
    hostname: str,
    processes: list[ProcessCreate],
    db: Session = Depends(get_db),
):
    try:
        return ProcessService.save_processes(
            db=db,
            hostname=hostname,
            processes=processes,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


# مهم: هاد Route خاصو يكون قبل /{asset_id}
@router.get("/{asset_id}/top/cpu")
def get_top_cpu_processes(
    asset_id: UUID,
    limit: int = Query(10, ge=1, le=50),
    db: Session = Depends(get_db),
):
    return ProcessService.get_top_cpu(
        db=db,
        asset_id=asset_id,
        limit=limit,
    )

@router.get("/{asset_id}/top/memory")
def get_top_memory_processes(
    asset_id: UUID,
    limit: int = Query(10, ge=1, le=50),
    db: Session = Depends(get_db),
):
    return ProcessService.get_top_memory(
        db=db,
        asset_id=asset_id,
        limit=limit,
    )

@router.get(
    "/{asset_id}",
    response_model=ProcessListResponse,
)
def get_asset_processes(
    asset_id: UUID,
    page: int = Query(1, ge=1),
    size: int = Query(100, ge=1),
    db: Session = Depends(get_db),
):
    processes, total = (
        ProcessService.get_asset_processes(
            db=db,
            asset_id=asset_id,
            page=page,
            size=size,
        )
    )

    return ProcessListResponse(
        items=processes,
        total=total,
        page=page,
        size=size,
    )