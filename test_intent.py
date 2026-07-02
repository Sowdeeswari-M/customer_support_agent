from agents.intent_agent import detect_intent

queries = [
    "What is your refund policy?",
    "My router has a red light",
    "I want to speak to a human agent"
]

for q in queries:
    print(q)
    print("Intent:", detect_intent(q))
    print("-" * 40)