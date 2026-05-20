import requests

class ChatOllama:
    def __init__(self, model="phi3"):
        self.url = "http://localhost:11434/api/generate"
        self.model = model

    def invoke(self, prompt: str) -> str:
        response = requests.post(self.url, json={
            "model": self.model,
            "prompt": prompt,
            "stream": False
        })
        data = response.json()
        return data.get("response", "SIN RESPUESTA")
