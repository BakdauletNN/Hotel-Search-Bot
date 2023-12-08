from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message


@bot.message_handler(state=UserInfoState.amount_child)
def child(message: Message) -> None:
    bot.send_message(message.chat.id, 'Кол-во детей')
    bot.set_state(message.from_user.id, UserInfoState.amount_child, message.chat.id)
    if message.text.isdigit():
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['child'] = message.text
    else:
        return bot.send_message(message.chat.id, 'Некорректный ввод')


@bot.message_handler(state=UserInfoState.age_child)
def age_children(message: Message) -> None:
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        if data.get('child'):
            bot.send_message(message.chat.id, 'Возраст детей')
            bot.set_state(message.from_user.id, UserInfoState.age_child, message.chat.id)
            if message.text.isdigit():
                data['child_age'] = message.text
                bot.send_message(message.chat.id, 'Хорошо, записал')
        else:
            bot.send_message(message.chat.id, 'Возраст может быть только числом')
