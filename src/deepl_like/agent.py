from src.deepl_like.llm_model import ChatOllama


llm = ChatOllama(model="phi3")

class TranslatorAgent:
    def __init__(self, llm):
        self.llm = llm

    # ---------------------------
    # Habilidad 1: Traducir
    # ---------------------------
    def translate(self, text: str, target: str) -> str:
        prompt = f"""
Eres un traductor profesional como DeepL.

Traduce el siguiente texto al {target}:
- Detecta automáticamente el idioma
- Traduce de forma natural (NO literal)
- Mantén el significado original
- Usa lenguaje fluido

Texto:
{text}
"""
        return self.llm.invoke(prompt)

    # ---------------------------
    # Habilidad 2: Mejorar
    # ---------------------------
    def improve_text(self, text: str) -> str:
        prompt = f"""
Mejora el siguiente texto:
- Corrige gramática
- Hazlo más claro
- Hazlo profesional

Texto:
{text}
"""
        return self.llm.invoke(prompt)

    # ---------------------------
    # Habilidad 3: Detectar idioma
    # ---------------------------
    def detect_language(self, text: str) -> str:
        prompt = f"""
Detecta el idioma del siguiente texto.
Responde solo con el idioma:

Texto:
{text}
"""
        return self.llm.invoke(prompt)

    # ---------------------------
    # Router (CLAVE PARA LA PROFE)
    # ---------------------------
    def act(self, task_type: str, data: dict) -> str:

        if task_type == "translate":
            return self.translate(data["text"], data["target"])

        elif task_type == "improve":
            return self.improve_text(data["text"])

        elif task_type == "detect":
            return self.detect_language(data["text"])

        else:
            return "Tarea no soportada"