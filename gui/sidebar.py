import os
import streamlit as st
from chatbot.chatbot import Chatbot
from chatbot.embedding import Embedder


class Sidebar:

    MODEL_OPTIONS = ["gpt-3.5-turbo", "gpt-4"]
    TEMPERATURE_MIN_VALUE = 0.0
    TEMPERATURE_MAX_VALUE = 1.0
    TEMPERATURE_DEFAULT_VALUE = 0.0
    TEMPERATURE_STEP = 0.01

    @staticmethod
    def about():
        about = st.sidebar.expander("Link al Repo 🔗")
        sections = [
            "#### App creada con [Langchain](https://github.com/hwchase17/langchain), [OpenAI]("
            "https://platform.openai.com/docs/models/gpt-3-5) y [Streamlit](https://github.com/streamlit/streamlit) "
            "⚡",
            "#### Link al código: [github.com/axcasas](https://github.com/axcasas)",
            "#### Seguime en [LinkedIn](https://www.linkedin.com/in/axel-casas/)",
            "#### Lee mis artículos en [Medium](https://medium.com/@axel.em.casas)"
        ]
        for section in sections:
            about.write(section)

    def model_selector(self):
        model = st.selectbox(label="Modelo", options=self.MODEL_OPTIONS)
        st.session_state["model"] = model

    @staticmethod
    def reset_chat_button():
        if st.button("Resetear chat"):
            st.session_state["reset_chat"] = True
        st.session_state.setdefault("reset_chat", False)

    def temperature_slider(self):
        temperature = st.slider(
            label="Temperatura",
            min_value=self.TEMPERATURE_MIN_VALUE,
            max_value=self.TEMPERATURE_MAX_VALUE,
            value=self.TEMPERATURE_DEFAULT_VALUE,
            step=self.TEMPERATURE_STEP,
        )
        st.session_state["temperature"] = temperature

    def show_options(self):
        with st.sidebar.expander("🛠️ Herramientas", expanded=True):
            self.reset_chat_button()
            self.model_selector()
            self.temperature_slider()
            st.session_state.setdefault("model", self.MODEL_OPTIONS[0])
            st.session_state.setdefault("temperature", self.TEMPERATURE_DEFAULT_VALUE)


class Utilities:
    @staticmethod
    def load_api_key():
        if os.path.exists(".env") and os.environ.get("OPENAI_API_KEY") is not None:
            user_api_key = os.environ["OPENAI_API_KEY"]
            st.sidebar.success("API key cargada desde .env", icon="🚀")
        else:
            user_api_key = st.sidebar.text_input(
                label="#### Tu OpenAI API key 👇", placeholder="Pegá tu OpenAI key acá, sk-", type="password"
            )
            if user_api_key:
                st.sidebar.success("API key cargada correctamente!", icon="🚀")
        return user_api_key

    @staticmethod
    def handle_upload():
        uploaded_file = st.sidebar.file_uploader("upload", type="pdf", label_visibility="collapsed")
        if uploaded_file is not None:
            pass
        else:
            st.sidebar.info(
                "Cargá tu PDF para empezar a chatear", icon="👆"
            )
            st.session_state["reset_chat"] = True
        return uploaded_file

    @staticmethod
    def setup_chatbot(uploaded_file, model, temperature):
        embeds = Embedder()
        with st.spinner("Iniciando chat..."):
            uploaded_file.seek(0)
            file = uploaded_file.read()
            vectors = embeds.getDocEmbeds(file, uploaded_file.name)
            chatbot = Chatbot(model, temperature, vectors)
        st.session_state["ready"] = True
        return chatbot
