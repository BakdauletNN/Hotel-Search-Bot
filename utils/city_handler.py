from loader import bot
from utils.low_price import city_info
from keyboards.keyboards import get_locations
from telebot.types import Message


def handle_city(message: Message) -> None:
    user_city = message.text.strip()
    locations = city_info(user_city)
    if locations:
        markup = get_locations(locations) # TODO передавать список словарей [{ID, название}, {ID, название}...]
        bot.send_message(message.chat.id, 'Выберите локацию из списка:',
                         reply_markup=markup)


    else:
        bot.send_message(message.chat.id, 'Города не найдены.')
