memory_store = []


def add_memory(text, role="context"):
    if not text:
        return

    memory_store.append({
        "text": text,
        "role": role
    })

    # límite para no romper RAM
    if len(memory_store) > 30:
        memory_store.pop(0)


def get_memory():
    return memory_store