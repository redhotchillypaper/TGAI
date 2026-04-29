from telethon import TelegramClient
from app.config import API_ID, API_HASH

# User client for reading/listening
user_client = TelegramClient('user_session', API_ID, API_HASH)

# Bot client for posting (add bot_token later)
bot_client = TelegramClient('bot_session', API_ID, API_HASH)
