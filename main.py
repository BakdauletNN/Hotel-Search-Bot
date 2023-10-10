from handlers.default_handlers.start import start_settings
from handlers.custom_handlers.low import low_command
from database import launcher_db
from loader import bot
from handlers.default_handlers import help


if __name__ == '__main__':
    bot.polling(none_stop=True)