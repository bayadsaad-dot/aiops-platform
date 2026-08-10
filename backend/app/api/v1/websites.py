from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from sqlalchemy.orm import Session

from app.database.deps import get_db
from app.services.website_service import WebsiteService
from app.schemas.website import (
    WebsiteCreate,
    WebsiteRead,
)

router = APIRouter(
    prefix="/api/v1/websites",
    tags=["Websites"],
)


@router.get(
    "/",
    response_model=list[WebsiteRead],
)
def get_websites(
    db: Session = Depends(get_db),
):
    return WebsiteService.get_websites(db)


@router.post(
    "/",
    response_model=WebsiteRead,
)
def create_website(
    data: WebsiteCreate,
    db: Session = Depends(get_db),
):
    try:
        return WebsiteService.create_website(
            db=db,
            name=data.name,
            url=data.url,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.delete("/{website_id}")
def delete_website(
    website_id: UUID,
    db: Session = Depends(get_db),
):
    try:
        return WebsiteService.delete_website(
            db=db,
            website_id=website_id,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.post("/check")
def check_all_websites(
    db: Session = Depends(get_db),
):
    return WebsiteService.check_all_websites(db)