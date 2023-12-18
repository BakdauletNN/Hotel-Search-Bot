from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message
from datetime import datetime,date

@bot.message_handler(state=UserInfoState.date_entry)
def entry_date(message: Message) -> None:
    try:
        entry_date = datetime.strptime(message.text, '%d.%m.%Y')

        if entry_date.date() >= date.today():
            with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
                data['entry'] = entry_date.strftime('%d.%m.%Y')

            bot.send_message(message.chat.id, 'Хорошо, Введите дату выезда')
            bot.set_state(message.from_user.id, UserInfoState.date_exit, message.chat.id)
        else:
            bot.send_message(message.chat.id, 'Введенная дата должна быть не ранее текущей даты. Попробуйте еще раз.')

    except ValueError:
        bot.send_message(message.chat.id, 'Некорректный формат даты. Введите дату в формате dd.mm.yyyy.')