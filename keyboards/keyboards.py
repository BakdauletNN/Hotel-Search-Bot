from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_locations(locations): # TODO принять [{ID, название}, {ID, название}...] сформировать кнопки
    keyboard = InlineKeyboardMarkup()
    for location in locations:
        if len(location) <= 64:
            callback_data = "callback_data:" + str(hash(location)) #TODO здесь подумайте какую строку сформировать, чтобы потом ловить ее в обработчике
            keyboard.add(InlineKeyboardButton(text=location, callback_data=callback_data))
    return keyboard
