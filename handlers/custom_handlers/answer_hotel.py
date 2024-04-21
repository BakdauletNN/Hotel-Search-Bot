from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message
from utils.hotels_type import get_date
from datetime import datetime,date


@bot.message_handler(state=UserInfoState.answer_hotel)
def send_hotels(message: Message) -> None:
    try:
        # проверка на то что введенная дата выезда не раньше текущей даты
        if  date.today() <= datetime.strptime(message.text, '%d.%m.%Y').date():
            # Получение данных пользователя и запись в них введенной даты выезда.
            with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
                data['exit'] = message.text
                bot.send_message(message.chat.id, 'Дата выезда записан, вот вам отели')

            # данные от user которые мы раньше хранили в data,
            # на основании этого будем предлогать отель передав data в функцию get_date
            result = get_date(data)
            bot.send_message(message.chat.id, result)


        else:
            bot.send_message(message.chat.id, 'Введенная дата должна быть не ранее текущей даты.'
                                              ' Попробуйте еще раз.')
    except ValueError:
        # обработка случая когда введенная пользователем строка не соответствует формату даты
        bot.send_message(message.chat.id, 'Некорректный формат даты. Введите дату в формате dd.mm.yyyy.')



