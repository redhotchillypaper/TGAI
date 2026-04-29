import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

SOURCE_CHANNEL = os.getenv("READ_CHANNEL_LINK")
POST_CHANNEL = os.getenv("CHANNEL_LINK")

AI_TOKEN = os.getenv("AI_API_KEY")
TEMP_DIR = "temp"