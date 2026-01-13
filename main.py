import asyncio
from telethon import TelegramClient, events



bot = TelegramClient('bot_session', api_id, api_hash)

@bot.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    await event.reply('hello')

async def main():
    await bot.start(bot_token=bot_token)
    print('Bot is running. Connected:', bot.is_connected())
    await bot.run_until_disconnected()

asyncio.run(main())
