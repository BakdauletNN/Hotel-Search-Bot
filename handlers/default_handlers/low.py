from aiogram import types
from loader import dp
from utils.low_price import city_info
from keyboards.keyboards import create_city_keyboard


@dp.message_handler(commands=['low'])
async def low_command(message: types.Message):
    user = await message.answer(f'Введите город')
    user_input = user.text
    results = await city_info(user_input)

    if results:
        await message.answer('Уточните пожалуйста:',create_city_keyboard(results))
    else:
        await message.answer('Города не найдены.')
