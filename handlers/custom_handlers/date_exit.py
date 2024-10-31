from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message
from datetime import datetime, date


@bot.message_handler(state=UserInfoState.date_exit)
def exit_date(message: Message) -> None:
    try:
        if date.today() <= datetime.strptime(message.text, '%d.%m.%Y').date():
            with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
                data['entry'] = message.text
            bot.send_message(message.chat.id, 'Entry date is recorded, enter departure date')
            bot.set_state(message.from_user.id, UserInfoState.get_hotels_amount, message.chat.id)
        else:
            bot.send_message(message.chat.id, 'The date entered must be no earlier than the current date. Try again.')
    except ValueError:
        bot.send_message(message.chat.id, 'Invalid date format. Enter the date in the format dd.mm.yyyy.')




