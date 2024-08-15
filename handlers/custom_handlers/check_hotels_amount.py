from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message
from datetime import datetime


@bot.message_handler(state=UserInfoState.get_hotels_amount)
def get_amount_hotels(message: Message):
    try:
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            if datetime.strptime(message.text, '%d.%m.%Y').date() > datetime.strptime(data.get('entry'), '%d.%m.%Y').date():
                data['exit'] = message.text

                bot.set_state(message.from_user.id, UserInfoState.photo, message.chat.id)
                bot.send_message(message.chat.id, 'Дата выезда записана, введите кол-во отелей, не больше 5')
            else:
                bot.send_message(message.chat.id, 'Дата выезда должна быть позже даты въезда. Попробуйте еще раз.')
    except ValueError:
        bot.send_message(message.chat.id, 'Некорректный формат даты. Введите дату в формате dd.mm.yyyy.')
