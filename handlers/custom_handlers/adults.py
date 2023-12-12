from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message


@bot.message_handler(state=UserInfoState.amount_adults)
def adults(message: Message) -> None:
    bot.send_message(message.chat.id, 'Кол-во взрослых')
    bot.set_state(message.from_user.id, UserInfoState.amount_adults, message.chat.id)
    if message.text.isdigit():
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['adults'] = message.text
    else:
        bot.send_message(message.chat.id, 'некорректный ввод')






