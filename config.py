import os
from dotenv import load_dotenv
from telethon import TelegramClient

load_dotenv()

API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')
POST_CHANNEL = os.getenv('CHANNEL_LINK')
SOURCE_CHANNEL = os.getenv('READ_CHANNEL_LINK')
AI_TOKEN = os.getenv('AI_API_KEY')

# User client for reading/listening
user_client = TelegramClient('user_session', API_ID, API_HASH)

# Bot client for posting (add bot_token later)
bot_client = TelegramClient('bot_session', API_ID, API_HASH)
