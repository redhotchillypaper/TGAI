# import asyncio
# from perplexity import Perplexity
from config import AI_TOKEN

# perplexity = Perplexity(api_key=AI_TOKEN)


# async def rephrase(text):
#     response = perplexity.chat.completions.create(
#         model="llama-3.1-sonar-small-128k-online",
#         messages=[
#             {"role": "user", "content": f"Rephrase this: {text}"}
#         ]
#     )
#     return response.choices[0].message.content



# result = asyncio.run(rephrase("BIG TEXT BIG NEWS\n TRUMP IS GAY, MACLEOD FINN IS NOW A PRESIDENT OF JAMAICA"))
# print(result)

import requests
from config import AI_TOKEN
async def ai_rephrase(text):
    url = "https://api.perplexity.ai/chat/completions"

    payload = {
        "model": "sonar",
        "messages": [
            {"role": "user", "content": f"""You are a creative Ukrainian text rephraser for Telegram.

1. Rephrase the text COMPLETELY - make it different but keep meaning
2. Add 2-4 relevant emojis/stickers to make it engaging
3. Output ONLY the rephrased text with emojis
4. NO [numbers] or metadata
5. Be creative - don't just translate word-for-word
6. Make it sound natural and Telegram-friendly

Original text: "{text}"

Rephrased (with emojis, NOTHING ELSE):"""

}
        ]
    }

    headers = {
        "Authorization": f"Bearer {AI_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    response_data = response.json()

    return response_data['choices'][0]['message']['content']

