# 🤖 Vionyx PolicyBot

PolicyBot is an AI-powered assistant built for **Vionyx Technologies** to help employees quickly find answers from internal company policies and documents.

Instead of manually searching through PDFs or internal portals, employees can simply ask a question in natural language and PolicyBot retrieves the most relevant policy information and provides a clear answer.

The project is built using a **Retrieval-Augmented Generation (RAG)** architecture where company documents are embedded, stored in a vector database, and retrieved when a user asks a question.

If PolicyBot cannot resolve the issue using the available policy documents, the user can raise a **help request directly through the interface**, which sends an email notification to the support team.

---

## 🚀 What This Project Does

PolicyBot allows employees to:

- Ask questions about company policies
- Retrieve accurate answers from internal documents
- View the document source used to generate the answer
- Raise a support request if the issue cannot be resolved

This makes internal knowledge much easier to access and reduces the time employees spend searching through documentation.

---

## 🧠 How It Works

The chatbot follows a Retrieval-Augmented Generation pipeline:

1. Company policy documents are loaded and processed
2. The documents are split into smaller chunks
3. Each chunk is converted into vector embeddings
4. The embeddings are stored in a **FAISS vector database**
5. When a user asks a question:
   - The system searches for the most relevant document chunks
   - These chunks are passed to a language model
   - The model generates an answer based on the retrieved context

This ensures answers are **grounded in the company documents** instead of relying only on the model’s general knowledge.

---

## 📂 Documents Used

PolicyBot currently uses the following internal documents:

- Leave Policy
- HR Policy
- IT Security Policy
- Data Privacy Policy
- Code of Conduct
- Company Overview

These documents form the knowledge base for the assistant.

---

## ✨ Key Features

- Enterprise policy chatbot
- Retrieval-Augmented Generation (RAG)
- Semantic document search
- Vector database using FAISS
- Source citation for answers
- Detection of questions outside policy scope
- Help request system with email notifications
- Simple and interactive chatbot interface

---

## 🛠 Technologies Used

- Python
- LangChain
- FAISS
- Sentence Transformers
- Hugging Face Transformers
- Streamlit / Gradio
- SMTP (Email Notification System)

---

## 📌 Example Questions

You can ask PolicyBot questions like:

- What are the working hours at Vionyx Technologies?
- How many sick leaves are allowed?
- What are the company data privacy guidelines?
- What are the employee conduct rules?

---

## 🎯 Purpose of the Project

This project demonstrates how **Generative AI and Retrieval-Augmented Generation can be used to build enterprise knowledge assistants**.

The goal is to show how AI systems can make internal company information easier to access while also supporting real business workflows like support requests.

---

## 👨‍💻 Author

Built as a **Generative AI / RAG project** to explore how AI assistants can improve access to internal company knowledge.
