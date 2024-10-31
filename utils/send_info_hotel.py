from utils.hotel_information import hotel_info
from utils.hotels_params import get_data
from database.add_to_db import add


def send_info(data: dict):
    result_str = ''
    result = None
    hotel_ids = None

    if data.get('command') == 'high':
        result_str += 'Expensive hotels\n'
        result, hotel_ids = get_data(data, sort_type="PROPERTY_CLASS")
    elif data.get('command') == 'low':
        result_str += 'Cheap hotels\n'
        result, hotel_ids = get_data(data, sort_type="PRICE_LOW_TO_HIGH")

    if not result:
        return 'An error occurred while retrieving hotel data.'
    if not hotel_ids:
        return 'We couldnt find any hotels matching your request..'

    add(data)

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
