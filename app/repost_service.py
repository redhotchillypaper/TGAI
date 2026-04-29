import os
from pathlib import Path

from app.config import POST_CHANNEL, TEMP_DIR
from app.ai_service import ai_rephrase


Path(TEMP_DIR).mkdir(exist_ok=True)


async def repost_single_message(bot_client, message):
    text = message.text or ""
    caption = await ai_rephrase(text) if text else None

    if message.media:
        media_file = await message.download_media(file=f"{TEMP_DIR}/")

        try:
            await bot_client.send_file(
                POST_CHANNEL,
                media_file,
                caption=caption
            )
        finally:
            if media_file and os.path.exists(media_file):
                os.remove(media_file)
    else:
        if text:
            await bot_client.send_message(
                POST_CHANNEL,
                await ai_rephrase(text)
            )


async def repost_album(bot_client, messages):
    files = []

    try:
        for msg in messages:
            if msg.media:
                file_path = await msg.download_media(file=f"{TEMP_DIR}/")
                files.append(file_path)

        first_text = messages[0].text or ""
        caption = await ai_rephrase(first_text) if first_text else None

        if files:
            await bot_client.send_file(
                POST_CHANNEL,
                files,
                caption=caption
            )
    finally:
        for file_path in files:
            if file_path and os.path.exists(file_path):
                os.remove(file_path)