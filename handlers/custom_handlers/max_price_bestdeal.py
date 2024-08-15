from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message


@bot.message_handler(state=UserInfoState.price_max)
def max_price_params(message: Message):
    if message.text.isdigit() and message.text is int or float:
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['price_max_bestdeal'] = message.text
        bot.set_state(message.from_user.id, UserInfoState.distance, message.chat.id)
        bot.send_message(message.chat.id, 'Макс цена записана, введите растояние от центра в км ')

    else:
        bot.send_message(message.chat.id, 'Некоректное значение ')



