from app.models.incident import Incident
from app.models.metric import Metric
from app.models.process import Process


class PromptBuilder:

    @staticmethod
    def build(
        incident: Incident,
        metric: Metric,
        processes: list[Process],
    ) -> str:

        process_list = "\n".join(
            [
                f"- {p.name} | CPU: {p.cpu_percent:.1f}% | Memory: {p.memory_percent:.1f}%"
                for p in processes
            ]
        )

        prompt = f"""
You are a Senior AIOps Engineer.

Analyze the following infrastructure incident.

=========================
INCIDENT
=========================

Title:
{incident.title}

Description:
{incident.description}

Priority:
{incident.priority.value}

Status:
{incident.status.value}

=========================
SYSTEM METRICS
=========================

CPU Usage:
{metric.cpu_usage:.2f}%

Memory Usage:
{metric.memory_usage:.2f}%

Disk Usage:
{metric.disk_usage:.2f}%

=========================
TOP RUNNING PROCESSES
=========================

{process_list}

=========================
YOUR TASK
=========================

Provide:

1. Summary
2. Root Cause
3. Impact on the system
4. Recommended actions
5. Confidence (0-100)

Return ONLY valid JSON.

Use this exact format:

{{
  "summary": "...",
  "root_cause": "...",
  "impact": "...",
  "confidence": 0,
  "recommendations": [
    "...",
    "...",
    "..."
  ]
}}

Rules:

- Do not use markdown.
- Do not use ```json.
- Do not add explanations.
- Return JSON only.
"""

        return prompt