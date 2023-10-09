from aiogram import types
from loader import dp


@dp.message_handler(commands=['start'])
async def start_settings(message: types.Message):
    user_name = message.from_user.first_name
    await message.answer(f'Здраствуйте, {user_name} !')
