import asyncio
from telethon import TelegramClient, events
from dotenv import load_dotenv
import os

load_dotenv() # loading .env

# TODO:
# Second section, divide the file into two
# real functions
# change text to POSTS



# .env variables:
api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')
link_to_channel = os.getenv('CHANNEL_LINK')

# session declaration 
bot = TelegramClient('bot_session', api_id, api_hash)


async def main():
    await bot.start(bot_token=bot_token)
    channel = await bot.get_entity(link_to_channel)
    print('Bot is running. Connected:', bot.is_connected())
    await bot.send_message(channel, "TEST TEXT") #change text to POSTS
    
    await bot.run_until_disconnected()


asyncio.run(main())

# for testing shi
@bot.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    await event.reply('hello')


#  (public) or 'https://t.me/+hash' for private. Join if required: from telethon.tl.functions.channels import JoinChannelRequest; await client(JoinChannelRequest(channel)).

# ​
# Posting Messages

# Require post permissions: await client.send_message(channel, 'Hello from bot!'). Supports text, media: await client.send_file(channel, photo, caption='Post'). Use silent=True to avoid notifications