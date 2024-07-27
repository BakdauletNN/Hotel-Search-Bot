from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message
from utils.bestdeal_params import get_data_bestdeal
from utils.hotel_information import hotel_info


@bot.message_handler(state=UserInfoState.distance)
def distance_from_center(message: Message):
    try:
        distance_km = float(message.text)
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['center_distance'] = distance_km
        bot.send_message(message.chat.id, 'Расстояние от центра записано. Ждите результаты...')
        result, hotel_ids = get_data_bestdeal(data)
        bot.send_message(message.chat.id, result)
        for hotel_id in hotel_ids:
            hotel_data = {"property_id": hotel_id, "photos": data.get('photos')}
            hotel_info_str, photo_urls = hotel_info(hotel_data)
            if hotel_info_str:
                bot.send_message(message.chat.id, hotel_info_str)
                for photo_url in photo_urls:
                    bot.send_photo(message.chat.id, photo_url)
    except ValueError:
        bot.send_message(message.chat.id, 'Некорректное значение, пожалуйста введите число.')
