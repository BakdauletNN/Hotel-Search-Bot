from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message
import re


@bot.message_handler(state=UserInfoState.date_entry)
def entry_date(message: Message) -> None:
    if re.match(r'^[\d\s]+$', message.text):
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['child_age'] = [int(age) for age in message.text.split()]
        bot.set_state(message.from_user.id, UserInfoState.date_exit, message.chat.id)
        bot.send_message(message.chat.id, 'Now enter the entry date in the format (04/01/2021)')
    else:
        bot.send_message(message.chat.id, 'Invalid input')




