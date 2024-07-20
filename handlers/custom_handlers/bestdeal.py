from keyboards.keyboards import get_locations
from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message
from utils.bestdeal_city import city_info_bestdeal


@bot.message_handler(commands=['bestdeal'])
def high_command(message: Message) -> None:
    # Сброс состояния
    bot.delete_state(message.from_user.id, message.chat.id)

    bot.set_state(message.from_user.id, UserInfoState.user_city, message.chat.id)
    bot.send_message(message.chat.id, 'Введите город')


@bot.message_handler(state=UserInfoState.user_city)
def get_user_city_bestdeal(message: Message) -> None:
    if message.text.isalpha():
        locations = city_info_bestdeal(message.text)
        markup = get_locations(locations)
        bot.send_message(message.chat.id, 'Выберите локацию из списка:', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Некорректный ввод')
