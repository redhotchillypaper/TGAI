import os
import asyncio
from collections import defaultdict
from telethon import TelegramClient, events
from dotenv import load_dotenv
from config import user_client, bot_client, SOURCE_CHANNEL, POST_CHANNEL
from ai_rephrase import ai_rephrase



async def post_posts(channel, text):
    await bot_client.send_message(channel, await ai_rephrase(text))


albums = defaultdict(list)

@user_client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    if not event.message.grouped_id:  # Single 
        if event.message.media:
            media_file = await event.download_media(file='temp/')
            await bot_client.send_file(POST_CHANNEL, media_file, caption= await ai_rephrase(event.message.text) or None)
            os.remove(media_file)
        else:
            await post_posts(POST_CHANNEL, event.message.text)
        return
    
    # Album: ONLY first msg starts task
    album_id = event.message.grouped_id
    albums[album_id].append(event.message)
    
    # Task only on FIRST msg
    if len(albums[album_id]) == 1:
        asyncio.create_task(process_album(album_id))
    return  # Later msgs SKIP processing

async def process_album(album_id):
    await asyncio.sleep(2)  # Full album
    
    album_msgs = albums[album_id][:]  # Snapshot
    albums[album_id].clear()  # Block dups IMMEDIATE
    
    if len(album_msgs) >= 2:
        files = []
        for msg in album_msgs:
            if msg.media:
                file_path = await msg.download_media(file='temp/')
                files.append(file_path)
        
        await bot_client.send_file(
            POST_CHANNEL,
            files,
            caption= await ai_rephrase(album_msgs[0].text) or None
        )
        
        for f in files:
            os.remove(f)
        
async def main():
    await user_client.start(phone=lambda: input('Phone: '))
    await bot_client.start()
    print(f"Listening {SOURCE_CHANNEL} → {POST_CHANNEL}")
    await asyncio.gather(
        user_client.run_until_disconnected(),
        bot_client.run_until_disconnected()
    )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nStopped")
