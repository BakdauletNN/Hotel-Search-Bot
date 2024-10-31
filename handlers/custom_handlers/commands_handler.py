from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message
import datetime
from utils.get_city_user import city_info
from keyboards.keyboards import get_locations
from utils.history import command_history


@bot.message_handler(commands=['low', 'high', 'bestdeal', 'history'])
def commands(message: Message):
    command = message.text.strip('/')
    if command == 'history':
        bot.delete_state(message.from_user.id, message.chat.id)
        answer_history = command_history(message)
        bot.send_message(message.from_user.id, answer_history)

    else:
        bot.delete_state(message.from_user.id, message.chat.id)
        bot.set_state(message.from_user.id, UserInfoState.user_city, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data.update({
                'user_id_telegram': message.from_user.id,
                'command': command,
                'location_id': None,
                'city': None,
                'adults': None,
                'children': None,
                'entry': None,
                'exit': None,
                'hotels_qty': None,
                'photos': None,
                'price_min_bestdeal': None,
                'price_max_bestdeal': None,
                'distance_from_center': None,
                'request_date': datetime.datetime.now().strftime('%Y-%m-%d'),
            })
            bot.send_message(message.chat.id, "Enter city:")


@bot.message_handler(state=UserInfoState.user_city)
def get_user_city(message: Message) -> None:
    if message.text.isalpha():
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['city'] = message.text
            locations = city_info(message.text)
            markup = get_locations(locations)
            bot.send_message(message.chat.id, 'Select a location from the list:', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Invalid input')
