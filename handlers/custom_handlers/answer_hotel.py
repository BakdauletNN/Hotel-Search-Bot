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
            bot.send_message(message.chat.id, 'Прошу ждать в течение минуты')

            result, hotel_ids = get_data(data)
            bot.send_message(message.chat.id, result)
            bot.send_message(message.chat.id, 'Нужны фотографии? (да/нет)')
            bot.register_next_step_handler(message, process_photo_response, hotel_ids)
        else:
            bot.send_message(message.chat.id, 'Введенная дата должна быть не ранее текущей даты. Попробуйте еще раз.')
    except ValueError:
        bot.send_message(message.chat.id, 'Некорректный формат даты. Введите дату в формате dd.mm.yyyy.')


def process_photo_response(message: Message, hotel_ids):
    if message.text.lower() == 'да':
        bot.send_message(message.chat.id, 'введите кол-во фотографий для каждого отеля, не больше 5')
        bot.register_next_step_handler(message, process_photo_amount, hotel_ids)
    else:
        process_hotels(message, hotel_ids, photo_amount=0)


def process_photo_amount(message: Message, hotel_ids):
    try:
        if message.text.isdigit() and 1 <= int(message.text) <= 5:
            photo_amount = int(message.text)
            process_hotels(message, hotel_ids, photo_amount)
        else:
            bot.send_message(message.chat.id, 'введите цифру от 1 до 5.')
            bot.register_next_step_handler(message, process_photo_amount, hotel_ids)
    except ValueError:
        bot.send_message(message.chat.id, 'Некорректное значение, введите цифру.')
        bot.register_next_step_handler(message, process_photo_amount, hotel_ids)


def process_hotels(message: Message, hotel_ids, photo_amount):
    for hotel_id in hotel_ids:
        hotel_data = {"property_id": hotel_id}
        hotel_info_str, photo_urls = hotel_info(hotel_data)

        if hotel_info_str:
            bot.send_message(message.chat.id, hotel_info_str)

            if photo_amount > 0:
                for photo_url in photo_urls[:photo_amount]:
                    bot.send_photo(message.chat.id, photo_url)
        else:
            bot.send_message(message.chat.id, f"Не удалось получить информацию для id: {hotel_id}")
