from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message
from datetime import datetime,date


@bot.message_handler(state=UserInfoState.date_entry)
def entry_date(message: Message) -> None:
    if message.text.isdigit():
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['child_age'] = message.text
        bot.set_state(message.from_user.id, UserInfoState.date_exit, message.chat.id)
        bot.send_message(message.from_user.id, 'Возраст записан. Теперь введите дата '
                                               'въезда в таком формате (01.04.2021)')
    else:
        bot.send_message(message.from_user.id, 'Возраст может быть только числом')

