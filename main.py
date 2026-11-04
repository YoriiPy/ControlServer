from aiogram import Dispatcher, Router, Bot
from dotenv import load_dotenv
from handlers import router
import asyncio
import os

async def main():
    load_dotenv()
    Token = os.getenv("BOT_TOKEN")

    bot = Bot(token=Token)

    dispatcher = Dispatcher()
    dispatcher.include_router(router)

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    print("Start Bot")
    asyncio.run(main())
