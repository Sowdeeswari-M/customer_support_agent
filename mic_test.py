import streamlit as st
from streamlit_mic_recorder import mic_recorder
import tempfile
import os

st.title("Mic Test")

audio = mic_recorder(
    start_prompt="🎤 Record",
    stop_prompt="⏹ Stop",
    key="mic"
)

if audio:
    st.success("Recording received!")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        f.write(audio["bytes"])
        audio_path = f.name

    st.write("Saved to:", audio_path)

    import os
    st.write("Exists:", os.path.exists(audio_path))
    st.write("Size:", os.path.getsize(audio_path))