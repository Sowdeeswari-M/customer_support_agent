from agents.orchestrator import orchestrate

queries = [
    "What are your working hours?",
    "My router has a red light.",
    "I want to speak to a human agent."
]

for q in queries:
    print("=" * 60)
    print("User:", q)
    print("Bot:", orchestrate(q))