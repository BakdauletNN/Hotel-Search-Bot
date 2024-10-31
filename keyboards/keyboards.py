from loguru import logger
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


@logger.catch()
def get_locations(locations):
    keyboard = InlineKeyboardMarkup()
    for location in locations:
        if len(location['name']) <= 64:
            callback_data = f"callback_data:{location['ID']}"
            keyboard.add(InlineKeyboardButton(text=location['name'], callback_data=callback_data))
    return keyboard

