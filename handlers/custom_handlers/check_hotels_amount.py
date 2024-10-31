from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message
from datetime import datetime


@bot.message_handler(state=UserInfoState.get_hotels_amount)
def get_amount_hotels(message: Message):
    try:
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            if datetime.strptime(message.text, '%d.%m.%Y').date() > datetime.strptime(data.get('entry'), '%d.%m.%Y').date():
                data['exit'] = message.text

                bot.set_state(message.from_user.id, UserInfoState.photo, message.chat.id)
                bot.send_message(message.chat.id, 'Departure date is recorded, enter the number of hotels, no more than 5')
            else:
                bot.send_message(message.chat.id, 'The departure date must be later than the entry date. try again.')
    except ValueError:
        bot.send_message(message.chat.id, 'Invalid date format. Enter the date in the format dd.mm.yyyy.')
