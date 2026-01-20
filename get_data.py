import os
import asyncio
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from dotenv import load_dotenv

# ────────────────────────────────────────────────
load_dotenv()

API_ID = int(os.getenv('API_ID') or 0)
API_HASH = os.getenv('API_HASH')
CHANNEL = os.getenv('READ_CHANNEL_LINK')          # @username or https://t.me/... or +1001234567890

SESSION_NAME = "userbot_session"                   # will create userbot_session.session

# Very important: never commit .session file or .env!
# ────────────────────────────────────────────────

async def main():
    if not all([API_ID, API_HASH, CHANNEL]):
        print("Missing API_ID, API_HASH or READ_CHANNEL_LINK in .env")
        return

    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

    try:
        await client.start()
        print("Client started successfully")

        # You can also do: await client.get_me() to see who you logged in as

        entity = await client.get_entity(CHANNEL)
        # print(f"Reading from: {entity.title or entity.username or CHANNEL}")

        # print("\nLast 10 messages:\n" + "─" * 50)

        async for msg in client.iter_messages(entity, limit=10):
            
            text_preview = (msg.text or "[no text]")[:70].replace("\n", " ")
            print(f"[{msg.id:>7}] {msg.date:%Y-%m-%d %H:%M}  {text_preview}")

    except SessionPasswordNeededError:
        print("2FA is enabled! Password needed.")
        password = input("Enter 2FA password: ")
        await client.sign_in(password=password)

    except Exception as e:
        print(f"Error: {type(e).__name__}: {e}")

    finally:
        await client.disconnect()
        print("\nDisconnected")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nStopped by user")