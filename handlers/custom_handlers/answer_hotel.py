from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message
from utils.hotels_type import get_date
from datetime import datetime,date


@bot.message_handler(state=UserInfoState.answer_hotel)
def send_hotels(message: Message) -> None:
    try:
        exit_config = datetime.strptime(message.text, '%d.%m.%Y')
        if exit_config.date() >= date.today():
            with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
                data['exit'] = exit_config.strftime('%d.%m.%Y')
            bot.send_message(message.chat.id, 'Дата выезда записана, вот вам отели', get_date())
        else:
            bot.send_message(message.chat.id, 'Введенная дата должна быть не ранее текущей даты.'
                                          ' Попробуйте еще раз.')
    except ValueError:
        bot.send_message(message.chat.id, 'Некорректный формат даты. Введите дату в формате dd.mm.yyyy.')



