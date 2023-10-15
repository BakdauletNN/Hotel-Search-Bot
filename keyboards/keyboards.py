from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_locations(locations):
    keyboard = InlineKeyboardMarkup()
    for location in locations:
        if len(location) <= 64:
            callback_data = "location:" + str(hash(location))
            keyboard.add(InlineKeyboardButton(text=location, callback_data=callback_data))
    return keyboard
