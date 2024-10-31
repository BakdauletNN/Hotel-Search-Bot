import telebot
from loader import bot


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.send_message(message.chat.id, f"Echo without state or filter.\nMessage: {message.text}")
