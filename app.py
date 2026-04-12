import streamlit as st
from chatbot import build_chain, chat

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="Groq Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 Groq Chatbot")
st.caption("Powered by LangChain + Groq open-source models")

# ── Sidebar settings ─────────────────────────────────────────────────────────
with st.sidebar:
    st.header("Settings")

    model_options = {
        "Llama 3.3 70B": "llama-3.3-70b-versatile",
        "Llama 3.1 8B": "llama-3.1-8b-instant",
        "Mixtral 8x7B": "mixtral-8x7b-32768",
        "Gemma2 9B": "gemma2-9b-it",
    }

    selected_label = st.selectbox("Model", list(model_options.keys()))
    selected_model = model_options[selected_label]

    temperature = st.slider("Temperature", 0.0, 1.0, 0.7, step=0.1)

    if st.button("Clear conversation"):
        st.session_state.messages = []
        st.session_state.chain = None
        st.rerun()

# ── Session state ─────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chain" not in st.session_state or st.session_state.get("current_model") != selected_model:
    st.session_state.chain = build_chain(selected_model, temperature)
    st.session_state.current_model = selected_model

# ── Render chat history ───────────────────────────────────────────────────────
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ── User input ────────────────────────────────────────────────────────────────
if user_input := st.chat_input("Type your message..."):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get and show assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat(st.session_state.chain, user_input)
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
