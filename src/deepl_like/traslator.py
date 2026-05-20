from src.Deepl_Like.llm_model import ChatModel

model = ChatModel()

def translate_text(text):
    return model.generate(text)
