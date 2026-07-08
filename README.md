# 🤖 Customer Support AI Agent

An AI-powered Customer Support Assistant built using a **Multi-Agent Architecture**, **Retrieval-Augmented Generation (RAG)**, **Voice Support**, and **Human Escalation**.

The system answers customer queries from a knowledge base, troubleshoots common internet issues, supports voice conversations, and escalates complex requests to a human support agent.

---

## 🚀 Features

- 🤖 Multi-Agent Workflow
- 📚 Retrieval-Augmented Generation (RAG)
- 🎤 Voice Input (Speech-to-Text using Faster Whisper)
- 🔊 Voice Output (ElevenLabs Text-to-Speech)
- 🛠️ Technical Troubleshooting
- 📖 FAQ Support
- 👨‍💼 Human Agent Escalation
- 💬 Interactive Chat Interface using Streamlit

---

## 🏗️ Architecture

```
                User
                  │
      ┌───────────┴───────────┐
      │                       │
   Text Input             Voice Input
                              │
                      Faster Whisper
                      (Speech-to-Text)
                              │
                       Intent Detection
                              │
                        Orchestrator
                              │
      ┌──────────┬────────────┴─────────────┐
      │          │             │            │
   RAG Agent   FAQ Agent  Troubleshooting  Escalation
                              │
                       Final Response
                              │
                     ElevenLabs TTS
                              │
                         Voice Output
```

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Faster Whisper
- ElevenLabs API
- LangChain
- FAISS Vector Database
- OpenRouter LLM
- HuggingFace Embeddings

---

## 📂 Project Structure

```
customer-support-agent/
│
├── agents/
│   ├── orchestrator.py
│   ├── intent_agent.py
│   ├── rag_agent.py
│   ├── troubleshooting_agent.py
│   └── escalation_agent.py
│
├── knowledge_base/
│
├── vectorstore/
│
├── app.py
├── voice.py
├── voice_input.py
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/customer-support-agent.git

cd customer-support-agent
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file and add:

```env
OPENROUTER_API_KEY=YOUR_API_KEY
ELEVENLABS_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🎯 Sample Queries

### 📚 FAQ

- What are your working hours?
- What is your refund policy?
- Tell me about your products.

### 🛠️ Troubleshooting

- My WiFi is not working.
- My internet is slow.
- My router shows a red light.

### 👨‍💼 Human Escalation

- I want to speak to a human agent.
- Connect me to support.

### 🎤 Voice

Speak your question through the microphone and receive both text and spoken responses.

---

## 📸 Demo

The application demonstrates:

- Multi-Agent Routing
- Intent Detection
- RAG-based Question Answering
- Voice Input
- Voice Output
- Human Escalation

---

## 🔮 Future Improvements

- LLM-based Intent Classification
- Conversation Memory
- CRM Integration
- Ticket Generation
- Sentiment Analysis
- Multilingual Support
- Live Agent Dashboard

---

## 👩‍💻 Author

**Sowdeeswari M**

B.E. Computer Science and Engineering

Sri Ramakrishna Engineering College

---

## 📄 License

This project is developed for educational and learning purposes.
