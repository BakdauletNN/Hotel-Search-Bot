from loader import bot
import re


@bot.callback_query_handler(func=lambda call: call.data.startswith("callback_data:"))
def handle_location_callback(call):
    chosen_city = re.search(r'callback_data:(.*)', call.data).group(1) # Получение выбранного города из данных обратного вызова
    bot.send_message(call.message.chat.id, f'id: {chosen_city}')
