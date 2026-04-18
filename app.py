import streamlit as st
from chatbot import build_chain, get_history, DEFAULT_SYSTEM_PROMPT

st.set_page_config(page_title="Groq Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 Groq Chatbot")
st.caption("Powered by LangChain + Groq open-source models")

# ── Sidebar settings ──────────────────────────────────────────────────────────
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
    system_prompt = st.text_area("System Prompt", value=DEFAULT_SYSTEM_PROMPT, height=100)

    if st.button("Clear conversation"):
        st.session_state.messages = []
        st.rerun()

# ── Session state ─────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chain is stateless — rebuild on every render with current sidebar values.
# History is managed explicitly so model/prompt switches never lose context.
chain = build_chain(selected_model, temperature, system_prompt)

# ── Render chat history ───────────────────────────────────────────────────────
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ── User input ────────────────────────────────────────────────────────────────
if user_input := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        history = get_history(st.session_state.messages[:-1])
        response = st.write_stream(
            chunk.content
            for chunk in chain.stream({"input": user_input, "history": history})
        )

    st.session_state.messages.append({"role": "assistant", "content": response})
