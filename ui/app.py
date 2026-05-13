import streamlit as st
from src.deepl_like.agent import TranslatorAgent
from src.deepl_like.llm_model import ChatOllama

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="DeepL Like",
    page_icon=" ",
    layout="wide"
)

# =========================
# ESTILOS
# =========================
st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

/* Fondo */
body {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

/* Título */
.title {
    font-size: 42px;
    font-weight: bold;
    text-align: center;
}

/* Subtítulo */
.subtitle {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 30px;
}

/* Tarjetas */
.card {
    background: #1e293b;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
}

/* Botón */
.stButton > button {
    background: linear-gradient(90deg, #3b82f6, #6366f1);
    color: white;
    border-radius: 10px;
    padding: 10px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.05);
}

/* Resultado */
.result-pro {
    background: linear-gradient(145deg, #020617, #0f172a);
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #334155;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.4);
    margin-top: 10px;
}

/* Texto resultado */
.result-text {
    font-size: 18px;
    color: #e2e8f0;
    line-height: 1.6;
    white-space: pre-wrap;
}

/* Historial */
.history-box {
    background: #020617;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# BACKEND
# =========================
llm = ChatOllama(model="phi3")
agent = TranslatorAgent(llm)

if "history" not in st.session_state:
    st.session_state.history = []

# =========================
# HEADER
# =========================
st.markdown('<div class="title"> DeepL Like</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Traductor inteligente con IA</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

# =========================
# ENTRADA
# =========================
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Texto de entrada")

    texto = st.text_area("", height=200, placeholder="Escribe aquí tu texto...")

    tarea = st.selectbox("¿Qué quieres hacer?", [
        "Traducir", "Mejorar", "Detectar idioma"
    ])

    idioma = st.selectbox("Idioma destino", [
        "English", "Spanish", "French", "German"
    ])

    ejecutar = st.button(" Ejecutar", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# SALIDA
# =========================
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Resultado")

    if ejecutar:

        if texto.strip() == "":
            st.warning("Escribe un texto primero")
        else:

            with st.spinner("Procesando con IA..."):

                if tarea == "Traducir":
                    resultado = agent.act("translate", {
                        "text": texto,
                        "target": idioma
                    })

                elif tarea == "Mejorar":
                    resultado = agent.act("improve", {
                        "text": texto
                    })

                elif tarea == "Detectar idioma":
                    resultado = agent.act("detect", {
                        "text": texto
                    })

            st.markdown(f"""
            <div class="result-pro">
                <div style="color:#94a3b8; font-size:14px; margin-bottom:10px;">
                </div>
                <div class="result-text">
                    {resultado}
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Guardar historial
            st.session_state.history.append({
                "input": texto,
                "output": resultado
            })

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# HISTORIAL
# =========================
st.markdown("## Historial reciente")

for item in reversed(st.session_state.history[-5:]):
    st.markdown(f"""
    <div class="history-box">
        <b>Entrada:</b><br>{item["input"]}<br><br>
        <b>Salida:</b><br>{item["output"]}
    </div>
    """, unsafe_allow_html=True)