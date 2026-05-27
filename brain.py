import requests
from memory import get_memory, add_memory

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"


def build_prompt(user_message: str):
    memory = get_memory()

    context = "\n".join(
        [f"- {m['text']}" for m in memory if "text" in m]
    )

    prompt = f"""
Eres una IA conversacional estable.

Reglas:
- No repitas frases innecesarias
- No saludes si ya hay conversación
- Responde SOLO al usuario
- Mantén coherencia

Memoria:
{context}

Usuario: {user_message}
IA:
"""
    return prompt


def ask_ai(user_message: str):
    prompt = build_prompt(user_message)

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    try:
        r = requests.post(OLLAMA_URL, json=payload)
        response = r.json()["response"]

    except Exception as e:
        response = f"Error conectando con Llama3: {e}"

    # guardar memoria (solo cosas útiles)
    add_memory(user_message, "user")
    add_memory(response, "assistant")

    return response