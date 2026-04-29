from collections import defaultdict
import asyncio

from telethon import events

from app.config import SOURCE_CHANNEL
from app.repost_service import repost_single_message, repost_album

albums = defaultdict(list)


def register_handlers(user_client, bot_client):
    @user_client.on(events.NewMessage(chats=SOURCE_CHANNEL))
    async def handler(event):
        message = event.message

        if not message.grouped_id:
            await repost_single_message(bot_client, message)
            return

        album_id = message.grouped_id
        albums[album_id].append(message)

        if len(albums[album_id]) == 1:
            asyncio.create_task(process_album(bot_client, album_id))


async def process_album(bot_client, album_id):
    await asyncio.sleep(2)

    album_messages = albums[album_id][:]
    albums.pop(album_id, None)

    await repost_album(bot_client, album_messages)