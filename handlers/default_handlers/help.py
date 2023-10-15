from loader import bot


@bot.message_handler(commands=['help'])
def bot_help(message):
    commands_list = "/start - Начать\n/low - Низкие цены"
    bot.send_message(message.chat.id, commands_list, parse_mode="Markdown")
