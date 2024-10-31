from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message


@bot.message_handler(state=UserInfoState.amount_child)
def child(message: Message) -> None:
    if message.text.lower() == 'no':
        bot.send_message(message.from_user.id, 'Got it, I don’t have any children with me. Enter your entry date')
        bot.set_state(message.from_user.id, UserInfoState.date_exit, message.chat.id)
    elif message.text.lower() == 'yes':
        bot.send_message(message.chat.id, 'Number of children')
        bot.set_state(message.from_user.id, UserInfoState.age_child, message.chat.id)
    else:
        bot.send_message(message.chat.id, 'Yes or No')


@bot.message_handler(state=UserInfoState.age_child)
def age_children(message: Message) -> None:
    if message.text.isdigit():
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['child_amount'] = message.text

        bot.set_state(message.from_user.id, UserInfoState.date_entry, message.chat.id)
        bot.send_message(message.chat.id, 'The number is recorded, Now enter the age of the children separated by a space')

    else:
        bot.send_message(message.chat.id, 'Qty can be a number')