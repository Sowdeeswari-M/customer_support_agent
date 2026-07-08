import streamlit as st
from agents.orchestrator import orchestrate
import traceback

try:
    import voice_input
    speech_to_text = voice_input.speech_to_text
except Exception:
    traceback.print_exc()
    raise
from voice import speak
import tempfile

st.set_page_config(
    page_title="Customer Support AI",
    page_icon="🤖",
    layout="wide"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- Sidebar ---------------- #

with st.sidebar:

    st.title("🤖 Support AI")

    st.divider()

    st.success("✔ Multi-Agent")
    st.success("✔ RAG")
    st.success("✔ Voice")
    st.success("✔ Human Escalation")

    st.divider()

    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ---------------- Header ---------------- #

st.title("🤖 Customer Support AI Agent")

st.caption(
    "Multi-Agent • RAG • Voice • ElevenLabs • Human Escalation"
)

st.divider()

# ---------------- Chat ---------------- #

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# =====================================================
# VOICE INPUT
# =====================================================

st.subheader("🎤 Voice Assistant")

audio = st.audio_input("Speak")

if audio is not None:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        f.write(audio.read())
        audio_path = f.name

    with st.spinner("🎤 Converting Speech..."):
        prompt = speech_to_text(audio_path)

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("🤖 Thinking..."):

        response = orchestrate(prompt)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":response
        }
    )

    with st.chat_message("assistant"):
        st.markdown(response)

    audio_file = speak(response)

    st.audio(audio_file)

# =====================================================
# TEXT CHAT
# =====================================================

prompt = st.chat_input("Ask me anything...")

if prompt:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Thinking..."):

        response = orchestrate(prompt)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":response
        }
    )

    with st.chat_message("assistant"):
        st.markdown(response)

    audio_file = speak(response)

    st.audio(audio_file)