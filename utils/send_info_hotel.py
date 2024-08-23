from utils.hotel_information import hotel_info
from utils.hotels_params import get_data


def send_info(data: dict):
    result_str = ''
    result = None
    hotel_ids = None

    if data.get('command') == 'high':
        result_str += 'Дорогие отели\n'
        result, hotel_ids = get_data(data, sort_type="PROPERTY_CLASS")
    elif data.get('command') == 'low':
        result_str += 'Дешевые отели\n'
        result, hotel_ids = get_data(data, sort_type="PRICE_LOW_TO_HIGH")

    if not result or not hotel_ids:
        return 'Произошла ошибка при получении данных отеля.'
    # сообщение со списком отелей
    messages = [result_str + result]
    for hotel_id in hotel_ids:
        hotel_data = {"property_id": hotel_id, "photos": data.get('photos')}
        hotel_info_str, photo_urls = hotel_info(hotel_data)

        if not hotel_info_str:
            continue

        detailed_message = hotel_info_str + "\n"

        if photo_urls and data.get('photos') > 0:
            messages.append(detailed_message)
            for photo_url in photo_urls:
                messages.append(('photo', photo_url))
        else:
            messages.append(detailed_message)
    return messages
