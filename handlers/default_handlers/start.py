import telebot
from loader import bot


@bot.message_handler(commands=['start'])
def start_settings(message):
    user_name = message.from_user.first_name
    bot.send_message(message.chat.id, f'Hello, {user_name}!')
