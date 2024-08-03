from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message


@bot.message_handler(state=UserInfoState.photo)
def hotels_amount(message: Message):
    try:
        if 1 <= int(message.text) <= 5:
            with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
                data['hotels_qty'] = message.text

                bot.set_state(message.from_user.id, UserInfoState.quantity_photo, message.chat.id)
                bot.send_message(message.chat.id, 'Кол-во отелей записана, нужны фото (да/нет)?')
        else:
            bot.send_message(message.chat.id, 'Кол-во отелей должно быть от 1 до 5')
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите числовое значение для количества отелей.')


