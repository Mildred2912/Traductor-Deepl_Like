from fastapi import FastAPI
from src.Deepl_Like.agent import TranslatorAgent
from src.Deepl_Like.llm_model import ChatOllama

app = FastAPI()

# Inicializar modelo y agente
llm = ChatOllama(model="phi3")
agent = TranslatorAgent(llm)

# -------------------------
# Endpoint de traducción
# -------------------------
@app.post("/translate")
def translate(data: dict):
    text = data["text"]
    target = data["target"]

    result = agent.act("translate", {
        "text": text,
        "target": target
    })

    return {"translation": result}
