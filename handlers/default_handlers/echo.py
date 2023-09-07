from aiogram import types
from loader import dp


@dp.message_handler(state=None)
async def echo_message(message: types.Message):
    await message.reply("Эхо без состояния или фильтра.\n" f"Сообщение: {message.text}")
