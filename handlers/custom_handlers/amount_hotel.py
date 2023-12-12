from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message


@bot.message_handler(state=UserInfoState.number_hotel)
def amount_hotel(message: Message) -> None:
    bot.send_message(message.chat.id, 'Кол-во отелей?')
    bot.set_state(message.from_user.id, UserInfoState.number_hotel, message.chat.id)
    if message.text.isdigit():
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['hotels_number'] = message.text
    else:
        bot.send_message(message.chat.id, 'некорректный ввод')