from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message


@bot.message_handler(state=UserInfoState.amount_child)
def child(message: Message) -> None:
    if message.text.lower() == 'да':
        bot.send_message(message.chat.id, 'Кол-во детей')
        bot.set_state(message.from_user.id, UserInfoState.age_child, message.chat.id)
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['child_amount'] = message.text
            bot.send_message(message.chat.id, 'Возраст детей')
    else:
        bot.send_message(message.chat.id, 'Хорошо, детей с собой нету')
        bot.send_message(message.chat.id, 'Введите дату въезда в формате (01.04.2021)')
        bot.set_state(message.from_user.id, UserInfoState.date_entry, message.chat.id)


@bot.message_handler(state=UserInfoState.age_child)
def age_children(message: Message) -> None:
    if message.text.isdigit():
        bot.send_message(message.chat.id, 'Возраст записан. Теперь введите дата '
                                          'въезда в таком формате (01.04.2021)')

        bot.set_state(message.from_user.id, UserInfoState.date_entry, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['child_age'] = message.text

    else:
        bot.send_message(message.chat.id, 'Возраст может быть только числом')