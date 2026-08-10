from uuid import UUID
import json

from sqlalchemy.orm import Session

from app.models.ai_analysis import AIAnalysis

from app.repositories.incident_repository import IncidentRepository
from app.repositories.metric_repository import MetricRepository
from app.repositories.process_repository import ProcessRepository
from app.repositories.ai_analysis_repository import AIAnalysisRepository

from app.services.ai.prompt_builder import PromptBuilder
from app.services.ai.providers.ollama_provider import OllamaProvider


class IncidentAnalyzer:

    @staticmethod
    def analyze(
        db: Session,
        incident_id: UUID,
    ):

        incident = IncidentRepository.get_by_id(
            db=db,
            incident_id=incident_id,
        )

        if not incident:
            raise ValueError("Incident not found.")

        metric = MetricRepository.get_latest_by_asset(
            db=db,
            asset_id=incident.asset_id,
        )

        if not metric:
            raise ValueError("No metrics found.")

        processes = ProcessRepository.get_top_cpu(
            db=db,
            asset_id=incident.asset_id,
            limit=10,
        )

        prompt = PromptBuilder.build(
            incident=incident,
            metric=metric,
            processes=processes,
        )

        provider = OllamaProvider()

        response = provider.chat(prompt)

        try:
            analysis = json.loads(response)

        except json.JSONDecodeError:

            analysis = {
                "summary": response,
                "root_cause": "",
                "impact": "",
                "confidence": 0,
                "recommendations": [],
            }

        existing = AIAnalysisRepository.get_by_incident(
            db=db,
            incident_id=incident.id,
        )

        root_cause = analysis.get("root_cause", "")
        if isinstance(root_cause, dict):
            root_cause = root_cause.get(
                "description",
                "",
            )

        impact = analysis.get("impact", [])
        if isinstance(impact, list):
            impact = "\n".join(impact)
        else:
            impact = str(impact)

        recommendations = analysis.get(
            "recommendations",
            [],
        )

        if isinstance(recommendations, list):
            recommendations_text = "\n".join(
                recommendations
            )
        else:
            recommendations_text = str(
                recommendations
            )

        if existing:

            existing.summary = analysis.get(
                "summary",
                "",
            )

            existing.root_cause = root_cause

            existing.impact = impact

            existing.confidence = analysis.get(
                "confidence",
                0,
            )

            existing.recommendations = (
                recommendations_text
            )

            AIAnalysisRepository.update(
                db=db,
                analysis=existing,
            )

        else:

            AIAnalysisRepository.create(
                db=db,
                analysis=AIAnalysis(
                    incident_id=incident.id,
                    summary=analysis.get(
                        "summary",
                        "",
                    ),
                    root_cause=root_cause,
                    impact=impact,
                    confidence=analysis.get(
                        "confidence",
                        0,
                    ),
                    recommendations=recommendations_text,
                ),
            )

        return {
            "incident_id": str(incident.id),
            "analysis": analysis,
        }