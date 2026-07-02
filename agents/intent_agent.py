def detect_intent(user_query):
    query = user_query.lower()

    # Escalation
    if any(word in query for word in [
        "human", "agent", "representative", "manager",
        "complaint", "escalate", "support person"
    ]):
        return "escalation"

    # Troubleshooting
    if any(word in query for word in [
        "not working", "issue", "problem", "error",
        "failed", "can't", "cannot", "red light",
        "slow", "internet", "router"
    ]):
        return "troubleshooting"

    # Default
    return "rag"