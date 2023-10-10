import telebot
from loader import bot


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.send_message(message.chat.id, f"Эхо без состояния или фильтра.\nСообщение: {message.text}")
