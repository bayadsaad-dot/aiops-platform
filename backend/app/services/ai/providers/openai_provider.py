from openai import OpenAI

from app.core.config import settings


class OpenAIProvider:

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY,
        )

        self.model = settings.OPENAI_MODEL

    def chat(self, prompt: str) -> str:

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an experienced AIOps engineer. "
                        "Analyze infrastructure incidents and provide "
                        "root cause analysis with recommendations."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0.2,
        )

        return response.choices[0].message.content