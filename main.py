from handlers.default_handlers.start import start_settings
from loader import  dp
from aiogram import executor
from handlers.default_handlers import low

if __name__ == '__main__':
    executor.start_polling(dp)
