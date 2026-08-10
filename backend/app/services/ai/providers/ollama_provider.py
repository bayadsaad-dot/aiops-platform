import requests


class OllamaProvider:

    def __init__(
        self,
        model: str = "llama3.2",
        base_url: str = "http://localhost:11434",
    ):
        self.model = model
        self.base_url = base_url

    def chat(self, prompt: str) -> str:

        print("Sending request to Ollama...")

        response = requests.post(
            f"{self.base_url}/api/chat",
            json={
                "model": self.model,
                "messages": [
                    {
                        "role": "system",
                        "content": (
                            "You are an expert AIOps engineer."
                        ),
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
                "stream": False,
            },
            timeout=300,
        )

        print("Status:", response.status_code)
        print("Response:", response.text)

        response.raise_for_status()

        return response.json()["message"]["content"]