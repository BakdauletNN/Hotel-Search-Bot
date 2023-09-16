from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def create_city_keyboard(city_names):
    keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [InlineKeyboardButton(city, callback_data=city) for city in city_names]
    keyboard.add(*buttons)
    return keyboard


