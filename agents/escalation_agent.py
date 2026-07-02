def escalation_agent(user_query):
    summary = f"""
Support Escalation Summary

Customer Issue:
{user_query}

Status:
Needs human assistance.

Recommended Action:
Assign to a customer support representative.
"""

    return summary