import os
import streamlit as st
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------
load_dotenv()

# LangSmith Tracing (Optional)
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY", "")
os.environ["LANGSMITH_PROJECT"] = "QnA ChatBot"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# --------------------------------------------------
# Prompt Template
# --------------------------------------------------
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful AI assistant. "
            "Provide accurate and concise answers."
        ),
        ("user", "{question}")
    ]
)

# --------------------------------------------------
# LLM Factory
# --------------------------------------------------
def get_llm(model_name, temperature, max_tokens):

    local_models = [
        "llama3.2:3b",
        "llama3.2:1b",
        "mistral",
        "qwen3:4b",
        "gemma3:4b"
    ]

    if model_name in local_models:
        return ChatOllama(
            model=model_name,
            temperature=temperature
        )

    return ChatOpenAI(
        model=model_name,
        api_key=OPENAI_API_KEY,
        temperature=temperature,
        max_tokens=max_tokens
    )

# --------------------------------------------------
# Response Generator
# --------------------------------------------------
def generate_response(question, model_name, temperature, max_tokens):

    llm = get_llm(
        model_name,
        temperature,
        max_tokens
    )

    chain = (
        prompt
        | llm
        | StrOutputParser()
    )

    return chain.invoke(
        {
            "question": question
        }
    )

# --------------------------------------------------
# Streamlit UI
# --------------------------------------------------
st.set_page_config(
    page_title="QnA ChatBot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 QnA ChatBot")
st.markdown("Ask anything using OpenAI or Ollama models.")

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.header("Settings")

selected_model = st.sidebar.selectbox(
    "Choose Model",
    [
        "gpt-4o-mini",
        "gpt-4o",
        "llama3.2:3b",
        "mistral",
        "qwen3:4b"
    ]
)

temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.7
)

max_tokens = st.sidebar.slider(
    "Max Tokens",
    min_value=100,
    max_value=4000,
    value=1000
)

# --------------------------------------------------
# User Input
# --------------------------------------------------
question = st.text_area(
    "Enter your question:",
    height=120
)

if st.button("Generate Response"):

    if not question.strip():
        st.warning("Please enter a question.")
    else:

        with st.spinner("Thinking..."):

            try:

                response = generate_response(
                    question,
                    selected_model,
                    temperature,
                    max_tokens
                )

                st.subheader("Response")
                st.write(response)

            except Exception as ex:

                st.error(
                    f"An error occurred:\n{str(ex)}"
                )

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.caption(
    "Powered by LangChain, OpenAI and Ollama"
) 
