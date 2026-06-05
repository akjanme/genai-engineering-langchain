import os
import time

import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.vectorstores import FAISS

# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# --------------------------------------------------
# LLM
# --------------------------------------------------
llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model_name="llama-3.1-8b-instant"
)

# --------------------------------------------------
# Prompt
# --------------------------------------------------
prompt = ChatPromptTemplate.from_template(
    """
    Answer the question based only on the provided context.

    <context>
    {context}
    </context>

    Question: {input}
    """
)

# --------------------------------------------------
# Vector Embedding Creation
# --------------------------------------------------
def create_vector_embedding():
    if "vectors" not in st.session_state:

        embeddings = OpenAIEmbeddings(
            api_key=OPENAI_API_KEY
        )

        loader = PyPDFDirectoryLoader("research_papers")

        docs = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        final_documents = text_splitter.split_documents(docs)

        vectors = FAISS.from_documents(
            final_documents,
            embeddings
        )

        st.session_state.embeddings = embeddings
        st.session_state.docs = docs
        st.session_state.final_documents = final_documents
        st.session_state.vectors = vectors


# --------------------------------------------------
# UI
# --------------------------------------------------
st.set_page_config(
    page_title="RAG Document Q&A",
    page_icon="📚"
)

st.title("📚 RAG Document Q&A using Groq + FAISS")

user_prompt = st.text_input(
    "Ask a question from your research papers"
)

if st.button("Create Vector Database"):
    with st.spinner("Creating embeddings..."):
        create_vector_embedding()

    st.success("Vector Database Created Successfully!")

# --------------------------------------------------
# Query
# --------------------------------------------------
if user_prompt:

    if "vectors" not in st.session_state:
        st.error(
            "Please create the vector database first."
        )
        st.stop()

    document_chain = create_stuff_documents_chain(
        llm,
        prompt
    )

    retriever = st.session_state.vectors.as_retriever(
        search_kwargs={"k": 4}
    )

    retrieval_chain = create_retrieval_chain(
        retriever,
        document_chain
    )

    start = time.time()

    response = retrieval_chain.invoke(
        {"input": user_prompt}
    )

    elapsed_time = time.time() - start

    st.write("### Answer")
    st.write(response["answer"])

    st.caption(
        f"Response Time: {elapsed_time:.2f} seconds"
    )

    with st.expander("Retrieved Documents"):
        for i, doc in enumerate(
            response["context"],
            start=1
        ):
            st.markdown(f"**Document {i}**")
            st.write(doc.page_content)
            st.divider()