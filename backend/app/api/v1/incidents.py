from uuid import UUID

from fastapi import APIRouter, Depends, Query, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.database.deps import get_db

from app.repositories.incident_repository import IncidentRepository
from app.repositories.ai_analysis_repository import AIAnalysisRepository

from app.services.incident_service import IncidentService
from app.services.ai.incident_analyzer import IncidentAnalyzer
from app.services.pdf_service import PDFService

from app.schemas.incident import (
    IncidentRead,
    IncidentListResponse,
)

router = APIRouter(
    prefix="/api/v1/incidents",
    tags=["Incidents"],
)


@router.get(
    "/",
    response_model=IncidentListResponse,
)
def get_incidents(
    page: int = Query(1, ge=1),
    size: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):

    incidents, total = IncidentService.get_incidents(
        db=db,
        page=page,
        size=size,
    )

    return IncidentListResponse(
        items=incidents,
        total=total,
        page=page,
        size=size,
    )


@router.get(
    "/{incident_id}",
    response_model=IncidentRead,
)
def get_incident(
    incident_id: UUID,
    db: Session = Depends(get_db),
):

    incident = IncidentRepository.get_by_id(
        db=db,
        incident_id=incident_id,
    )

    if not incident:
        raise HTTPException(
            status_code=404,
            detail="Incident not found.",
        )

    return incident


# ==========================
# GET AI ANALYSIS
# ==========================

@router.get("/{incident_id}/analysis")
def get_analysis(
    incident_id: UUID,
    db: Session = Depends(get_db),
):

    analysis = AIAnalysisRepository.get_by_incident(
        db=db,
        incident_id=incident_id,
    )

    if not analysis:
        raise HTTPException(
            status_code=404,
            detail="AI analysis not found.",
        )

    return analysis


# ==========================
# ANALYZE INCIDENT
# ==========================

@router.post(
    "/{incident_id}/analyze",
)
def analyze_incident(
    incident_id: UUID,
    db: Session = Depends(get_db),
):
    try:

        return IncidentAnalyzer.analyze(
            db=db,
            incident_id=incident_id,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e),
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# ==========================
# DOWNLOAD PDF REPORT
# ==========================

@router.get("/{incident_id}/report")
def download_report(
    incident_id: UUID,
    db: Session = Depends(get_db),
):

    incident = IncidentRepository.get_by_id(
        db=db,
        incident_id=incident_id,
    )

    if not incident:
        raise HTTPException(
            status_code=404,
            detail="Incident not found",
        )

    analysis = AIAnalysisRepository.get_by_incident(
        db=db,
        incident_id=incident_id,
    )

    if not analysis:
        raise HTTPException(
            status_code=404,
            detail="AI analysis not found",
        )

    pdf = PDFService.build(
        incident,
        analysis,
    )

    return StreamingResponse(
        pdf,
        media_type="application/pdf",
        headers={
            "Content-Disposition": (
                f'attachment; filename="incident-{incident.id}.pdf"'
            ),
        },
    )