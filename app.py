
import streamlit as st

st.set_page_config(page_title="Vionyx PolicyBot")

st.title("🤖 Vionyx PolicyBot")
st.write("Enterprise Policy Assistant for Vionyx Technologies")

# Chat section
question = st.text_input("Ask your question")

if question:

    answer, sources = agent(question)

    st.write("### 🤖 PolicyBot Response")
    st.write(answer)

    if sources:
        st.write("### 📄 Sources")
        for s in sources:
            st.write(s)

st.write("---")

# Help request section
st.write("### 🆘 Raise Help Request")

name = st.text_input("Employee Name")
issue = st.text_area("Describe your issue")

if st.button("Send Request"):
    result = send_help_request(name, issue)
    st.success(result)
