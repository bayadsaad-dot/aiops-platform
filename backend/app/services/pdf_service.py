from io import BytesIO

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate


class PDFService:

    @staticmethod
    def build(incident, analysis):

        buffer = BytesIO()

        doc = SimpleDocTemplate(buffer)

        styles = getSampleStyleSheet()

        elements = []

        elements.append(
            Paragraph("<b>AIOps Incident Report</b>", styles["Title"])
        )

        elements.append(
            Paragraph(f"<b>Incident:</b> {incident.title}", styles["Heading2"])
        )

        elements.append(
            Paragraph(f"<b>Priority:</b> {incident.priority.value}", styles["BodyText"])
        )

        elements.append(
            Paragraph(f"<b>Status:</b> {incident.status.value}", styles["BodyText"])
        )

        elements.append(
            Paragraph("<br/><b>Summary</b>", styles["Heading2"])
        )

        elements.append(
            Paragraph(analysis.summary, styles["BodyText"])
        )

        elements.append(
            Paragraph("<br/><b>Root Cause</b>", styles["Heading2"])
        )

        elements.append(
            Paragraph(analysis.root_cause, styles["BodyText"])
        )

        elements.append(
            Paragraph("<br/><b>Impact</b>", styles["Heading2"])
        )

        elements.append(
            Paragraph(analysis.impact, styles["BodyText"])
        )

        elements.append(
            Paragraph(
                f"<br/><b>Confidence:</b> {analysis.confidence}%",
                styles["BodyText"],
            )
        )

        elements.append(
            Paragraph("<br/><b>Recommendations</b>", styles["Heading2"])
        )

        for item in analysis.recommendations.split("\n"):
            elements.append(
                Paragraph(f"• {item}", styles["BodyText"])
            )

        doc.build(elements)

        buffer.seek(0)

        return buffer