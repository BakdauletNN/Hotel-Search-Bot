from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message


@bot.message_handler(state=UserInfoState.amount_child)
def child(message: Message) -> None:
    if message.text.lower() == 'нет':
        return UserInfoState.date_entry
    elif message.text.lower() == 'да':
        bot.send_message(message.chat.id, 'Кол-во детей')
        bot.state(message.from_user.id, UserInfoState.age_child, message.chat.id)


@bot.message_handler(state=UserInfoState.age_child)
def age_children(message: Message) -> None:
    if message.text.isdigit():
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['child_amount'] = message.text
        bot.send_message(message.chat.id, 'Кол-во записана, Теперь введите возраст')
        bot.set_state(message.from_user.id, UserInfoState.date_entry, message.chat.id)
    else:
        bot.send_message(message.chat.id, 'Кол-во может быть числом')