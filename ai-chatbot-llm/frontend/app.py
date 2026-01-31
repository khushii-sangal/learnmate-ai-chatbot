import streamlit as st
import requests

st.set_page_config(page_title="LearnMate AI", page_icon="📘")

st.title("📘 LearnMate AI")
st.markdown("💡 *Ask questions, revise concepts, or get motivation!*")

st.subheader("Your AI Study Assistant")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask me anything about your studies...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Send request to backend
    try:
        response = requests.post(
            "https://learnmate-ai-chatbot.onrender.com/chat",
            json={"message": user_input}
        )

        bot_reply = response.json()["response"]

    except Exception:
        bot_reply = "⚠️ Sorry, I couldn't connect to the backend."

    # Show bot message
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
