from handlers.default_handlers.start import start_settings
from handlers.custom_handlers.low import low_command
from loader import bot
from telebot import types

@bot.message_handler(commands=['help'])
def bot_help(message):
    commands_list = "/start - Начать\n/low - Низкие цены"
    bot.send_message(message.chat.id, commands_list, parse_mode="Markdown")
