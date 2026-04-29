import httpx

OLLAMA_URL = "http://localhost:11434/api/generate"

async def ai_rephrase(text: str) -> str:
    if not text:
        return ""

    prompt = """You are a creative Ukrainian text rephraser for Telegram.

Rules:
1. Rephrase completely but keep the meaning.
2. Make it natural, punchy, Telegram-friendly.
3. Add 2-4 relevant emojis.
4. Output ONLY the final text.
5. No metadata, no explanations, no [numbers].

Original text:
{text}
"""

    async with httpx.AsyncClient(timeout=120) as client:
        response = await client.post(
            OLLAMA_URL,
            json={
                "model": "llama3.1",
                "prompt": prompt,
                "stream": False
            }
        )
        response.raise_for_status()

    return response.json()["response"].strip()