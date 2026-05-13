import requests

class ChatOllama:
    def __init__(self, model="phis3"):
        self.url = "http://localhost:11434/api/generate"
        self.model = model

    def invoke(self, prompt: str) -> str:
        response = requests.post(self.url, json={
            "model": self.model,
            "prompt": prompt,
            "stream": False
            })
        print(response.json())  
        data = response.json()
        return data.get("response", "SIN RESPUESTA")