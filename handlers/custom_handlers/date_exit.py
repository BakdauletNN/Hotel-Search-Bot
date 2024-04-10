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
            bot.set_state(message.from_user.id, UserInfoState.answer_hotel, message.chat.id)
            bot.send_message(message.chat.id, 'Дата въезда записана, введите дата выезда')
        else:
            bot.send_message(message.chat.id, 'Введенная дата должна быть не ранее текущей даты.'
                                          ' Попробуйте еще раз.')
    except ValueError:
        bot.send_message(message.chat.id, 'Некорректный формат даты. Введите дату в формате dd.mm.yyyy.')




