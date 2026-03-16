import streamlit as st
import os
import re
import smtplib
from email.mime.text import MIMEText

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


# -----------------------------
# Load Documents
# -----------------------------

loader = DirectoryLoader(
    "documents",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

documents = loader.load()


# -----------------------------
# Text Splitting
# -----------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)


# -----------------------------
# Embeddings
# -----------------------------

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_documents(chunks, embedding_model)

retriever = vectorstore.as_retriever()


# -----------------------------
# LLM
# -----------------------------

model_name = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


def llm(prompt):

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    outputs = model.generate(
        **inputs,
        max_new_tokens=100
    )

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return answer


# -----------------------------
# Helper Functions
# -----------------------------

def normalize_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.strip()


# -----------------------------
# Agent
# -----------------------------

def agent(question):

    q = normalize_text(question)

    greetings = ["hi", "hello", "hey", "hii"]
    thanks = ["thanks", "thank you", "thankyou", "thx"]

    if q in greetings:
        return (
            "Hello! 👋 I'm PolicyBot, the AI assistant for Vionyx Technologies. You can ask me about company policies or HR guidelines.",
            []
        )

    if q in thanks:
        return (
            "You're welcome! 😊 Feel free to ask if you need more help regarding Vionyx policies.",
            []
        )

    docs = retriever.invoke(question)

    if not docs:
        return (
            "I couldn't find relevant information in the policy documents. Please raise a help request below.",
            []
        )

    context = ""
    sources = []

    for doc in docs:

        context += doc.page_content + "\n"

        file_name = os.path.basename(doc.metadata["source"])
        page = doc.metadata["page"] + 1

        sources.append(f"{file_name} (Page {page})")


    prompt = f"""
You are PolicyBot, an AI assistant for Vionyx Technologies.

Use the company policy documents to answer the question clearly.

Context:
{context}

Question: {question}

Answer briefly.
"""

    answer = llm(prompt)

    return answer, list(set(sources))


# -----------------------------
# Email Help Request
# -----------------------------

def send_help_request(name, issue):

    sender_email = "rjking1577@gmail.com"
    sender_password = "igfv zmaz dpqa yeqw"

    receiver_email = "rajajaiswal1577@gmail.com"

    message = MIMEText(f"""
New Help Request from Vionyx PolicyBot

Employee Name: {name}

Issue Description:
{issue}
""")

    message["Subject"] = "Vionyx PolicyBot Help Request"
    message["From"] = sender_email
    message["To"] = receiver_email

    try:

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(sender_email, sender_password)

        server.sendmail(sender_email, receiver_email, message.as_string())

        server.quit()

        return "✅ Help request sent successfully."

    except Exception as e:

        return f"❌ Failed to send request: {e}"


# -----------------------------
# STREAMLIT UI
# -----------------------------

st.set_page_config(page_title="Vionyx PolicyBot", layout="wide")

st.title("🤖 Vionyx PolicyBot")
st.write("Enterprise Policy Assistant for Vionyx Technologies")


# Chat Section

st.subheader("💬 Ask your question")

question = st.text_input(
    "Ask about company policies",
    placeholder="Example: How many sick leaves are allowed?"
)

if question:

    answer, sources = agent(question)

    st.write("### 🤖 PolicyBot Response")

    st.success(answer)

    if sources:

        st.write("### 📄 Sources")

        for s in sources:
            st.write("-", s)


st.divider()


# Help Request Section

with st.expander("🆘 Raise Help Request"):

    name = st.text_input("Employee Name")

    issue = st.text_area("Describe your issue")

    if st.button("Send Request"):

        result = send_help_request(name, issue)

        st.success(result)
