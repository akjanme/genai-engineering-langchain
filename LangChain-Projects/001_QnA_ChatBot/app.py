import streamlit as st
import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# LangSmith Tracing
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_PROJECT"] = "QnA ChatBot with OpenAI"

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that answers questions accurately."
        ),
        ("user", "Question: {question}")
    ]
)

def generate_response(question, api_key, model_name, temperature, max_tokens):

    llm = ChatOpenAI(
        model=model_name,
        api_key=api_key,
        temperature=temperature,
        max_tokens=max_tokens
    )

    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser

    return chain.invoke({"question": question})


# UI
st.title("QnA ChatBot with OpenAI")

st.sidebar.title("Settings")

api_key = os.getenv("OPENAI_API_KEY")

# Model Selection
model_name = st.sidebar.selectbox(
    "Select Model",
    ["gpt-4o", "gpt-4o-mini", "gpt-3.5-turbo"]
)

temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.5
)

max_tokens = st.sidebar.slider(
    "Max Tokens",
    min_value=50,
    max_value=2000,
    value=500
)

st.write("Ask a question:")

user_input = st.text_input("Your Question")

if user_input:
    try:
        response = generate_response(
            user_input,
            api_key,
            model_name,
            temperature,
            max_tokens
        )

        st.subheader("Answer")
        st.write(response)

    except Exception as e:
        st.error(f"Error: {str(e)}")
else:
    st.info("Please enter a question.")