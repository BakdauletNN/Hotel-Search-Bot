from aiogram import Bot,Dispatcher,executor,types
import os
from dotenv import load_dotenv
import config
from low_price import city_info
from keyboards import create_city_keyboard


load_dotenv()
bot_token = Bot(os.getenv('BOT_TOKEN'))
dp_bot = Dispatcher(bot=bot_token)


@dp_bot.message_handler(commands=['start'])
async def start_settings(message: types.Message):
    user_name = message.from_user.first_name
    await message.answer(f'Здраствуйте, {user_name} !')


@dp_bot.message_handler(commands=['search'])
async def search(message: types.Message):
    user = await message.answer(f'Введите город:')
    user_input = user.text
    results = await city_info(user_input)

    if results:
        city_keyboard = create_city_keyboard(results)
        await message.answer('Уточните пожалуйста:', reply_markup=city_keyboard)
    else:
        await message.answer('Города не найдены.')



if __name__ == '__main__':
    executor.start_polling(dp_bot)
    