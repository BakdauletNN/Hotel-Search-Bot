from loader import bot
import handlers
from database.history import command_history
from utils.set_bot_commands import set_default_commands
from database import models


if __name__ == '__main__':
    set_default_commands(bot)
    bot.infinity_polling()
