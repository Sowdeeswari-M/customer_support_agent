def detect_intent(query):
    query = query.lower()

    troubleshooting_keywords = [
        "wifi",
        "wi-fi",
        "internet",
        "router",
        "network",
        "connection",
        "not working",
        "slow",
        "disconnect",
        "offline",
        "signal",
    ]

    if any(word in query for word in troubleshooting_keywords):
        return "troubleshoot"

    if any(word in query for word in ["refund", "policy", "price", "product"]):
        return "faq"

    if any(word in query for word in ["human", "agent", "support", "complaint"]):
        return "escalate"

    return "rag"