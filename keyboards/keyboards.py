from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_locations(locations):
    keyboard = InlineKeyboardMarkup()
    for location in locations:
        keyboard.add(InlineKeyboardButton(text=location, callback_data=f"location:{location}"))
    return keyboard
