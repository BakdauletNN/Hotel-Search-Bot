from utils.low_price import city_info
from keyboards.keyboards import get_locations
from loader import bot


active_handlers = {}


@bot.message_handler(commands=['low'])
def low_command(message):
    user = bot.send_message(message.chat.id, 'Введите город')
    handler_id = message.chat.id

    @bot.message_handler(func=lambda msg: msg.text and msg.text.strip(), content_types=['text'])
    def handle_city(message):
        user_city = message.text.strip()
        locations = city_info(user_city)
        if locations:
            markup = get_locations(locations)
            bot.send_message(message.chat.id, 'Выберите город из списка:', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Города не найдены.')


