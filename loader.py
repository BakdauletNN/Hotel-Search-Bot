from loguru import logger
from telebot import TeleBot, custom_filters
from telebot.storage import StateMemoryStorage
from config_data import config

logger.add('debug.log', format="{time} {level} {message}")
storage = StateMemoryStorage()
bot = TeleBot(token=config.BOT_TOKEN, state_storage=storage)
bot.add_custom_filter(custom_filters.StateFilter(bot))
