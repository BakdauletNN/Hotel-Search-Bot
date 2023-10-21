from loader import bot
from handlers.custom_handlers.city_handler import handle_city
from states.contact_information import UserInfoState
from telebot.types import Message


active_handlers = {}


@bot.message_handler(commands=['low'])
def low_command(message: Message) -> None:
    bot.set_state(message.from_user.id, UserInfoState.user_city, message.chat.id)


@bot.message_handler(state=UserInfoState.user_city)
def get_user_city(message: Message) -> None:
    message = bot.send_message(message.chat.id, 'Введите город')
    if message.text.isalpha():
        handler_id = message.chat.id
        active_handlers[handler_id] = handle_city

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['user_city'] = message.text
    else:
        bot.send_message(message.chat.id, 'Город может содержать только буквы')
