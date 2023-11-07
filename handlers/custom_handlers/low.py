from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message
from utils.city_handler import handle_city


@bot.message_handler(commands=['low'])
def low_command(message: Message) -> None:
    bot.set_state(message.from_user.id, UserInfoState.user_city, message.chat.id)
    bot.send_message(message.chat.id, 'Введите город')


@bot.message_handler(state=UserInfoState.user_city)
def get_user_city(message: Message) -> None:
    # bot.send_message(message.chat.id, message.text)

    if message.text.isalpha():
        handle_city(message)
    else:
        bot.send_message(message.chat.id, 'Город может содержать только буквы')
