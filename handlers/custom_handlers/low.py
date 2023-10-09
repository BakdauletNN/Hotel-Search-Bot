from aiogram import types
from loader import dp
from keyboards.keyboards import get_locations
from utils.low_price import city_info

@dp.message_handler(commands=['low'])
async def low_command(message: types.Message):
    # Отправляем пользователю сообщение и ожидаем ответа о городе
    user = await message.answer(f'Введите город')

    # Создаем обработчик, который будет ждать ответ от пользователя
    @dp.message_handler(lambda msg: msg.text and msg.text.strip(), content_types=types.ContentTypes.TEXT)
    async def handle_city(message: types.Message):
        # Получаем введенный пользователем город
        user_city = message.text.strip()

        # Получаем список локаций для введенного города
        locations = await city_info(user_city)

        if locations:
            # Предоставляем пользователю выбор локации с помощью инлайн клавиатуры
            await message.reply('Выберите город из списка:', reply_markup=get_locations(locations))
        else:
            await message.reply('Города не найдены.')

        # Удаляем обработчик после завершения этапа выбора города
        dp.remove_handler(handle_city)

    # Указываем, что ждем ответа о городе
    dp.register_message_handler(handle_city)
