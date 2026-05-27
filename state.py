conversation_state = {
    "mode": "chat",   # chat | test | repeat | idle
    "topic": None,
    "last_ai": "",
    "last_user": "",
    "turns": 0
}


def update_state(user_text, intent):
    global conversation_state

    conversation_state["last_user"] = user_text
    conversation_state["turns"] += 1

    if intent == "stop":
        conversation_state["mode"] = "idle"
        conversation_state["topic"] = None

    elif intent in ["test", "repeat"]:
        conversation_state["mode"] = intent

    else:
        conversation_state["mode"] = "chat"

    # tracking simple de tema
    if conversation_state["topic"] is None:
        conversation_state["topic"] = intent
    elif intent != conversation_state["topic"]:
        conversation_state["topic"] = intent


def get_state():
    return conversation_state