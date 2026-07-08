from agents.intent_agent import detect_intent
from agents.rag_agent import rag_agent
from agents.troubleshooting_agent import troubleshooting_agent
from agents.escalation_agent import escalation_agent


def orchestrate(user_query):
    intent = detect_intent(user_query)

    if intent == "rag":
        return rag_agent(user_query)

    elif intent == "troubleshoot":
        return troubleshooting_agent(user_query)

    elif intent == "escalate":
        return escalation_agent(user_query)

    elif intent == "faq":
        return rag_agent(user_query)

    return "Sorry, I couldn't understand your request."