from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message
from utils.hotel_information import hotel_info
from utils.hotels_params import get_data
from loguru import logger
from database.models import History


@bot.message_handler(state=UserInfoState.final)
def send_info(message: Message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        if 'photos' not in data or data['photos'] == 0:
            if message.text.isdigit() and 1 <= int(message.text) <= 5:
                data['photos'] = int(message.text)
            else:
                data['photos'] = 0

        required_fields = ['command', 'location_id', 'city', 'adults', 'entry_date', 'exit_date', 'hotels_qty', 'photos']
        if all(data.get(field) is not None for field in required_fields):
            History.create(
                user_id=message.from_user.id,
                command=data['command'],
                city=data['city'],
                location_id=data['location_id'],
                adults_qty=data['adults'],
                children=data['children'],
                entry_date=data['entry_date'],
                exit_date=data['exit_date'],
                hotels_quantity=data['hotels_qty'],
                photo_qty=data['photos'],
                min_price=data.get('min_price'),
                max_price=data.get('max_price'),
                distance_from_center=data.get('distance_from_center'),
                request_date=data['request_date']
            )

        result = None
        hotel_ids = None

        if data.get('command') == 'high':
            bot.send_message(message.chat.id, 'Дорогие отели')
            result, hotel_ids = get_data(data, sort_type="PROPERTY_CLASS")
        elif data.get('command') == 'low':
            bot.send_message(message.chat.id, 'Дешевые отели')
            result, hotel_ids = get_data(data, sort_type="PRICE_LOW_TO_HIGH")
        elif data.get('command') == 'bestdeal':
            bot.set_state(message.from_user.id, UserInfoState.price_min, message.chat.id)
            bot.send_message(message.chat.id, 'Введите минимальную стоимость в долларах')
            return

        if result and hotel_ids:
            bot.send_message(message.chat.id, result)
            for hotel_id in hotel_ids:
                hotel_data = {"property_id": hotel_id, "photos": data.get('photos')}
                hotel_info_str, photo_urls = hotel_info(hotel_data)
                if hotel_info_str:
                    bot.send_message(message.chat.id, hotel_info_str)
                    for photo_url in photo_urls:
                        bot.send_photo(message.chat.id, photo_url)
                else:
                    logger.error(f"Ошибка: {hotel_id}")
        else:
            logger.error("Не удалось найти")
            bot.send_message(message.chat.id, 'Нет доступных отелей по вашему запросу.')
