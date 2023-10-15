from loader import bot
from handlers.custom_handlers.city_handler import handle_city


active_handlers = {}

@bot.message_handler(commands=['low'])
def low_command(message):
    user = bot.send_message(message.chat.id, 'Введите город')
    handler_id = message.chat.id
    active_handlers[handler_id] = handle_city
