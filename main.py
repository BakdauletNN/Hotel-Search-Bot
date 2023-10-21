from handlers.default_handlers.start import start_settings
from handlers.custom_handlers import low
from database import launcher_db
from loader import bot
from handlers.default_handlers import help
from telebot.custom_filters import StateFilter


if __name__ == '__main__':
    bot.add_custom_filter(StateFilter(bot))
    bot.infinity_polling()