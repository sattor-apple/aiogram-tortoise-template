import asyncio
import logging
import handlers

from loader import bot, dp
from tortoise import Tortoise
from configs import BotSettings

from middlewares import Register, Throttle

class Controller:
    async def __aenter__(self):
        await Tortoise.init(
            db_url=BotSettings.DATABASE_URL.get_secret_value(),
            modules={"models": ["database.models"]},
        )
        await dp.start_polling(bot)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await bot.session.close()
        await Tortoise.close_connections()


async def main():
    try:
        dp.update.middleware.register(Throttle())
        dp.update.middleware.register(Register())
        async with Controller() as controller:
            pass
    finally:
        pass


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
