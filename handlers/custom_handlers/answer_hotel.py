from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message
from utils.hotels_type import get_date
from datetime import datetime,date


@bot.message_handler(state=UserInfoState.answer_hotel)
def send_hotels(message: Message) -> None:
    """
    :param message:
    :return: None
    Здесь точно также как и с датой въезда
    """
    exit_config = datetime.strptime(message.text, '%d.%m.%Y')
    if exit_config.date() >= date.today():
        bot.send_message(message.chat.id, 'Дата выезда записана')


        """
        
        Тут только часть кода, остальная в процессе разработки
        """
        # try:
        bot.send_message(message.chat.id, 'Вот вам отели')
        with bot.retrieve_data(message.from_user.id, UserInfoState.answer_hotel, message.chat.id) as data:
            data['answer'] = message.text

        # except ValueError:
        #     bot.send_message(message.chat.id, 'Некорректный формат даты. Введите дату в формате dd.mm.yyyy.')
    else:
        bot.send_message(message.chat.id, 'Введенная дата должна быть не ранее текущей даты. Попробуйте еще раз.')



