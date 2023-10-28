from loader import bot
from utils.low_price import city_info
from keyboards.keyboards import get_locations
from states.contact_information import UserInfoState
from telebot.types import Message


@bot.message_handler(state=UserInfoState.city_list)
def handle_city(message: Message) -> None:
    user_city = message.text.strip()
    locations = city_info(user_city)
    if locations:
        markup = get_locations(locations)
        bot.send_message(message.chat.id, 'Выберите локацию из списка:',
                         reply_markup=markup)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['city_list'] = message.text

    else:
        bot.send_message(message.chat.id, 'Города не найдены.')
