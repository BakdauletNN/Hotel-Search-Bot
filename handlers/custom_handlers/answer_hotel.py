from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message
from datetime import datetime
from utils.low_price_params import get_data
from utils.high_price_params import get_high_price_data
from utils.hotel_information import hotel_info
from utils.bestdeal_params import get_data_bestdeal


@bot.message_handler(state=UserInfoState.answer_hotel)
def send_hotels(message: Message):
    try:
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            entry_date = datetime.strptime(data.get('entry'), '%d.%m.%Y').date()
            if datetime.strptime(message.text, '%d.%m.%Y').date() > entry_date:
                data['exit'] = message.text
                bot.send_message(message.chat.id, 'Дата выезда записана, вот вам отели')
                bot.send_message(message.chat.id, 'Прошу ждать в течение минуты')

                if data.get('command') == 'bestdeal':
                    bot.send_message(message.chat.id, 'Введите минимальную цену:')
                    bot.register_next_step_handler(message, get_min_price)
                elif data.get('command') == 'high':
                    result, hotel_ids = get_high_price_data(data)
                    bot.send_message(message.chat.id, result)
                    bot.send_message(message.chat.id, 'Нужны фотографии? (да/нет)')
                    bot.register_next_step_handler(message, process_photo_response, hotel_ids)
                else:
                    result, hotel_ids = get_data(data)
                    bot.send_message(message.chat.id, result)
                    bot.send_message(message.chat.id, 'Нужны фотографии? (да/нет)')
                    bot.register_next_step_handler(message, process_photo_response, hotel_ids)
            else:
                bot.send_message(message.chat.id, 'Дата выезда должна быть позже даты въезда. Попробуйте еще раз.')

    except ValueError:
        bot.send_message(message.chat.id, 'Некорректный формат даты. Введите дату в формате dd.mm.yyyy.')


def get_min_price(message: Message):
    try:
        min_price = float(message.text)
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['price_min'] = min_price
        bot.send_message(message.chat.id, 'Введите максимальную цену:')
        bot.register_next_step_handler(message, get_max_price)
    except ValueError:
        bot.send_message(message.chat.id, 'Некорректное значение, введите число.')
        bot.register_next_step_handler(message, get_min_price)


def get_max_price(message: Message):
    try:
        max_price = float(message.text)
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['price_max'] = max_price
            result, hotel_ids = get_data_bestdeal(data)
            bot.send_message(message.chat.id, result)
            bot.send_message(message.chat.id, 'Нужны фотографии? (да/нет)')
            bot.register_next_step_handler(message, process_photo_response, hotel_ids)
    except ValueError:
        bot.send_message(message.chat.id, 'Некорректное значение, введите число.')
        bot.register_next_step_handler(message, get_max_price)


def process_photo_response(message: Message, hotel_ids):
    if message.text.lower() == 'да':
        bot.send_message(message.chat.id, 'Введите количество фотографий для каждого отеля, не больше 5')
        bot.register_next_step_handler(message, process_photo_amount, hotel_ids)
    else:
        process_hotels(message, hotel_ids, photo_amount=0)


def process_photo_amount(message: Message, hotel_ids):
    try:
        if message.text.isdigit() and 1 <= int(message.text) <= 5:
            photo_amount = int(message.text)
            process_hotels(message, hotel_ids, photo_amount)
        else:
            bot.send_message(message.chat.id, 'Введите цифру от 1 до 5.')
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

    bot.delete_state(message.from_user.id, message.chat.id)
