from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message


@bot.message_handler(state=UserInfoState.amount_adults)
def adults_amount(message: Message) -> None:
    if message.text.isdigit():
        bot.set_state(message.from_user.id, UserInfoState.amount_child, message.chat.id)
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['adults'] = message.text
        bot.send_message(message.chat.id, 'Имеется ли у вас дети? (да/нет)')
    else:
        bot.send_message(message.chat.id, 'Некорректный ввод')




