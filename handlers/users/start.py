from aiogram import filters
from aiogram import types
from laoder import bot, dp


@dp.message(filters.CommandStart())
async def start(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Salom, dunyo!"
    )
