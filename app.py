import streamlit as st
from agents.orchestrator import orchestrate

st.set_page_config(
    page_title="Customer Support AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------
# Session State
# ------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ------------------------
# Sidebar
# ------------------------

with st.sidebar:

    st.title("🤖 Support AI")

    st.markdown("---")

    st.subheader("Capabilities")

    st.success("✔ Product Information")
    st.success("✔ Technical Troubleshooting")
    st.success("✔ FAQ Assistance")
    st.success("✔ Voice Support")
    st.success("✔ Human Escalation")

    st.markdown("---")

    st.subheader("Quick Actions")

    if st.button("📦 Product Information"):
        st.session_state.messages.append(
            {"role":"user","content":"Tell me about your products"}
        )

    if st.button("💳 Refund Policy"):
        st.session_state.messages.append(
            {"role":"user","content":"What is your refund policy?"}
        )

    if st.button("🌐 Internet Issues"):
        st.session_state.messages.append(
            {"role":"user","content":"My internet is not working"}
        )

    if st.button("🧹 Clear Chat"):
        st.session_state.messages=[]
        st.rerun()

# ------------------------
# Header
# ------------------------

st.title("🤖 Customer Support AI Agent")

st.caption(
    "AI-powered customer support with RAG, Multi-Agent Workflow, Voice Support & Human Escalation"
)

st.divider()

# ------------------------
# Chat History
# ------------------------

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ------------------------
# Bottom Input Area
# ------------------------

col1,col2=st.columns([8,1])

with col1:

    prompt=st.chat_input("Ask me anything...")

with col2:

    st.button("🎤")

# ------------------------
# Handle Input
# ------------------------

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