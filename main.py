from handlers.default_handlers.start import start_settings
from loader import dp
from aiogram import executor
from handlers.default_handlers.low import low_command
from database import launcher_db

if __name__ == '__main__':
    executor.start_polling(dp)
