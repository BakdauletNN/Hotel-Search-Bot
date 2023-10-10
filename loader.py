import telebot
from config_data import config


API_TOKEN = config.BOT_TOKEN
bot = telebot.TeleBot(API_TOKEN)