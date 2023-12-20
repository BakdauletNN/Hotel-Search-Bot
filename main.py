from loader import bot
import handlers
from utils.set_bot_commands import set_default_commands
from utils import date_config

if __name__ == '__main__':
    set_default_commands(bot)
    bot.infinity_polling()