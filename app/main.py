import asyncio

from app.clients import user_client, bot_client
from app.config import BOT_TOKEN, SOURCE_CHANNEL, POST_CHANNEL
from app.handlers import register_handlers


async def main():
    await user_client.start(phone=lambda: input("Phone: "))
    await bot_client.start(bot_token=BOT_TOKEN)

    register_handlers(user_client, bot_client)

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