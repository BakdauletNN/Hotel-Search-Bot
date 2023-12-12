from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message


@bot.message_handler(state=UserInfoState.date_entry)
def entry_date(message: Message) -> None:
    bot.send_message(message.chat.id, 'Введите дата въезда')
    bot.set_state(message.from_user.id, UserInfoState.date_entry, message.chat.id)
    if message.text.isdigit():
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['entry'] = message.text
    else:
        bot.send_message(message.chat.id, 'некорректный ввод')
