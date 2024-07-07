from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message
from datetime import datetime, date
from utils.hotels_type import get_data
from utils.hotel_information import hotel_info


@bot.message_handler(state=UserInfoState.answer_hotel)
def send_hotels(message: Message):
    try:
        if date.today() <= datetime.strptime(message.text, '%d.%m.%Y').date():
            with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
                data['exit'] = message.text
            bot.send_message(message.chat.id, 'Дата выезда записана, вот вам отели')
            bot.send_message(message.chat.id, 'Прошу ждать в течении минуты')

            result, hotel_ids = get_data(data)
            bot.send_message(message.chat.id, result)

            # Вызов функции hotel_info для каждого отеля
            for hotel_id in hotel_ids:
                hotel_data = {"id_hotel": hotel_id}  # Создаем словарь с идентификатором отеля
                hotel_details = hotel_info(hotel_data)
                bot.send_message(message.chat.id, hotel_details)

        else:
            bot.send_message(message.chat.id, 'Введенная дата должна быть не ранее текущей даты. Попробуйте еще раз.')
    except ValueError:
        bot.send_message(message.chat.id, 'Некорректный формат даты. Введите дату в формате dd.mm.yyyy.')
