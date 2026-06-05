import os
import tempfile

import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

from langchain.chains import (
    create_history_aware_retriever,
    create_retrieval_chain,
)
from langchain.chains.combine_documents import (
    create_stuff_documents_chain,
)

from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)

from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS

from langchain_text_splitters import RecursiveCharacterTextSplitter

# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------

load_dotenv()

# --------------------------------------------------
# Embeddings
# --------------------------------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# --------------------------------------------------
# Streamlit UI
# --------------------------------------------------

st.title("Conversational RAG With PDF Uploads & Chat History")
st.write("Upload PDFs and chat with their content.")

api_key = st.text_input(
    "Enter your Groq API Key",
    type="password"
)

if not api_key:
    st.warning("Please enter your Groq API Key")
    st.stop()

# --------------------------------------------------
# LLM
# --------------------------------------------------

llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama-3.3-70b-versatile",
    temperature=0
)

# --------------------------------------------------
# Session Management
# --------------------------------------------------

session_id = st.text_input(
    "Session ID",
    value="default_session"
)

if "store" not in st.session_state:
    st.session_state.store = {}

# --------------------------------------------------
# PDF Upload
# --------------------------------------------------

uploaded_files = st.file_uploader(
    "Choose PDF files",
    type="pdf",
    accept_multiple_files=True
)

if uploaded_files:

    documents = []

    with st.spinner("Processing PDFs..."):

        for uploaded_file in uploaded_files:

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".pdf"
            ) as temp_file:

                temp_file.write(uploaded_file.getvalue())
                temp_pdf_path = temp_file.name

            try:
                loader = PyPDFLoader(temp_pdf_path)
                docs = loader.load()
                documents.extend(docs)

            finally:
                if os.path.exists(temp_pdf_path):
                    os.remove(temp_pdf_path)

    if not documents:
        st.error("No content could be extracted from the uploaded PDFs.")
        st.stop()

    # --------------------------------------------------
    # Split Documents
    # --------------------------------------------------

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    splits = text_splitter.split_documents(documents)

    st.write(f"Documents Loaded: {len(documents)}")
    st.write(f"Chunks Created: {len(splits)}")

    if not splits:
        st.error("No text chunks were created from the PDFs.")
        st.stop()

    # --------------------------------------------------
    # Vector Store (FAISS)
    # --------------------------------------------------

    vectorstore = FAISS.from_documents(
        documents=splits,
        embedding=embeddings
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 4}
    )

    # --------------------------------------------------
    # Contextual Question Reformulation
    # --------------------------------------------------

    contextualize_q_system_prompt = """
    Given a chat history and the latest user question
    which may reference previous conversation context,
    reformulate it into a standalone question.

    Do not answer the question.
    """

    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}")
        ]
    )

    history_aware_retriever = create_history_aware_retriever(
        llm,
        retriever,
        contextualize_q_prompt
    )

    # --------------------------------------------------
    # QA Prompt
    # --------------------------------------------------

    system_prompt = """
    You are an assistant for question-answering tasks.

    Use the provided context to answer the question.

    If the answer is not available in the context,
    say you do not know.

    Keep the answer concise and under 5 sentences.

    Context:
    {context}
    """

    qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}")
        ]
    )

    question_answer_chain = create_stuff_documents_chain(
        llm,
        qa_prompt
    )

    rag_chain = create_retrieval_chain(
        history_aware_retriever,
        question_answer_chain
    )

    # --------------------------------------------------
    # Chat History
    # --------------------------------------------------

    def get_session_history(
        session: str,
    ) -> BaseChatMessageHistory:

        if session not in st.session_state.store:
            st.session_state.store[session] = ChatMessageHistory()

        return st.session_state.store[session]

    conversational_rag_chain = RunnableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history",
        output_messages_key="answer"
    )

    # --------------------------------------------------
    # User Question
    # --------------------------------------------------

    user_input = st.text_input(
        "Ask a question about the uploaded PDFs"
    )

    if user_input:

        response = conversational_rag_chain.invoke(
            {"input": user_input},
            config={
                "configurable": {
                    "session_id": session_id
                }
            }
        )

        st.write("### Answer")
        st.write(response["answer"])