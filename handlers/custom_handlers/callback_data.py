from loader import bot
from states.contact_information import UserInfoState
from utils.city_handler import handle_city
import re


@bot.callback_query_handler(func=lambda call: call.data.startswith("callback_data:"))
def handle_location_callback(call):
    chosen_city = re.search(r'callback_data:(.*)', call.data).group(1) # Получение выбранного города из данных обратного вызова
    handle_city(call.message)
    bot.send_message(call.message.chat.id, f'Вы выбрали город: {chosen_city}')
