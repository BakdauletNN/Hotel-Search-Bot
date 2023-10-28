from loader import bot
from handlers.custom_handlers.city_handler import handle_city
from states.contact_information import UserInfoState
from telebot.types import Message


@bot.message_handler(commands=['low'])
def low_command(message: Message) -> None:
    bot.set_state(message.from_user.id, UserInfoState.user_city, message.chat.id)
    bot.send_message(message.chat.id, 'Введите город')


@bot.message_handler(state=UserInfoState.user_city)
def get_user_city(message: Message) -> None:
    bot.send_message(message.chat.id, message.text)

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        if message.text.isalpha():
            data['user_city'] = message.text
            handle_city(message)
        else:
            bot.send_message(message.chat.id, 'Город может содержать только буквы')
