from loader import bot
from utils.low_price import city_info
from keyboards.keyboards import get_locations


def handle_city(message):
    user_city = message.text.strip()
    locations = city_info(user_city)
    if locations:
        markup = get_locations(locations)
        bot.send_message(message.chat.id, 'Выберите город из списка:', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Города не найдены.')
