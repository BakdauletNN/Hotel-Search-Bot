from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message
from utils.hotel_information import hotel_info
from utils.low_price_params import get_data
from utils.high_price_params import get_data_high
from database import database


@bot.message_handler(state=UserInfoState.final)
def send_info(message: Message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        if 'photos' not in data or data['photos'] == 0:
            data['photos'] = 0
        elif message.text.isdigit() and 1 <= int(message.text) <= 5:
            data['photos'] = int(message.text)
        else:
            bot.send_message(message.chat.id, 'Введите количество фотографий от 1 до 5.')
            return

        if data.get('command') == 'high':
            bot.send_message(message.chat.id, 'Дорогие отели')
            result, hotel_ids = get_data_high(data)
        elif data.get('command') == 'low':
            bot.send_message(message.chat.id, 'Дешевые отели')
            result, hotel_ids = get_data(data)
        elif data.get('command') == 'bestdeal':
            bot.set_state(message.from_user.id, UserInfoState.price_min, message.chat.id)
            bot.send_message(message.chat.id, 'Введите мин стоимость в долларах')
            return

        # Сохраняем историю в базу данных
        database.add_history(
            user_id=message.from_user.id,
            command=data.get('command'),
            city=data.get('city', 'None'),
            entry_date=data.get('entry'),
            exit_date=data.get('exit'),
            adults=data.get('adults'),
            children=data.get('child_age', []),
            location_id=data.get('id_location'),
            hotels_qty=data.get('hotels_qty'),
            photos=data.get('photos'),
            min_price=data.get('price_min_bestdeal'),
            max_price=data.get('price_max_bestdeal'),
            distance_from_center=data.get('center_distance')
        )

        bot.send_message(message.chat.id, result)
        for hotel_id in hotel_ids:
            hotel_data = {"property_id": hotel_id, "photos": data.get('photos')}
            hotel_info_str, photo_urls = hotel_info(hotel_data)
            if hotel_info_str:
                bot.send_message(message.chat.id, hotel_info_str)
                for photo_url in photo_urls:
                    bot.send_photo(message.chat.id, photo_url)
