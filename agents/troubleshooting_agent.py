def troubleshooting_agent(user_query):
    query = user_query.lower()

    if "red light" in query or "router" in query:
        return (
            "Let's troubleshoot your router:\n\n"
            "1. Restart the router.\n"
            "2. Check the WAN cable.\n"
            "3. Wait 2 minutes.\n"
            "4. If the issue continues, perform a factory reset.\n\n"
            "Did this solve your issue?"
        )

    if "slow" in query:
        return (
            "Try these steps:\n\n"
            "1. Restart your router.\n"
            "2. Move closer to the router.\n"
            "3. Restart your modem.\n"
            "4. Check with your ISP.\n\n"
            "Is the issue fixed?"
        )

    return "I couldn't identify the issue. I'll connect you with support if needed."