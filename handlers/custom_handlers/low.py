from keyboards.keyboards import get_locations
from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message

from utils.low_price import city_info


@bot.message_handler(commands=['low'])
def low_command(message: Message) -> None:
    bot.set_state(message.from_user.id, UserInfoState.user_city, message.chat.id)
    bot.send_message(message.chat.id, 'Введите город')


@bot.message_handler(state=UserInfoState.user_city)
def get_user_city(message: Message) -> None:
    if message.text.isalpha():
        locations = city_info(message.text)
        markup = get_locations(locations)  # TODO передавать список словарей [{ID, название}, {ID, название}...]
        bot.send_message(message.chat.id, 'Выберите локацию из списка:', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Город может содержать только буквы')
