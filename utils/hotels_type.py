from loguru import logger
from config_data.config import API_KEY
import requests
from handlers.custom_handlers.callback_data import handle_location_callback
from handlers.custom_handlers.adults import adults
from handlers.custom_handlers.entry_data import entry_date
from handlers.custom_handlers.date_exit import exit_date
from handlers.custom_handlers.answer_hotel import send_hotels


api = {'X-RapidApi-Key': API_KEY, 'X-RapidAPI-Host': "hotels4.p.rapidapi.com"}


class APIError(Exception):
    pass


@logger.catch()
def get_data(data: dict):

    exit_date = data.get('entry')  # Получаем строку с датой въезда
    entry_day, entry_month, entry_year = map(int, exit_date.split('.'))

    send_hotels = data.get('exit')
    exit_day, exit_month, exit_year = map(int, send_hotels.split('.'))

    adults = data.get('adults')
    entry_date = data.get('child_age')
    handle_location_callback = data.get('id_location')

    url = "https://hotels4.p.rapidapi.com/properties/v2/list"
    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "destination": {"regionId": handle_location_callback},
        "checkInDate": {
            "day": entry_day,
            "month": entry_month,
            "year": entry_year
        },
        "checkOutDate": {
            "day": exit_day,
            "month": exit_month,
            "year": exit_year
        },
        "rooms": [
            {
                "adults": int(adults),
                "children": [{"age": age} for age in entry_date]
            }
        ],
        "resultsStartingIndex": 0,
        "resultsSize": 200,
        "sort": "PRICE_LOW_TO_HIGH",

    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        if response.status_code == requests.codes.ok:
            json_data = response.json()
            properties = json_data.get("data", {}).get("propertySearch", {}).get("properties", [])
            hotel_info = []
            for i, property_data in enumerate(properties[:5]):
                hotel_name = properties[i]["name"]
                hotel_id = properties[i]['id']
                hotel_info.append({
                    "Отель": i + 1,
                    "Имя отеля": hotel_name,
                    "ID отеля": hotel_id
                })

            result = "\n".join([f"Отель {info['Отель']}: {info['Имя отеля']},"
                                  f" ID: {info['ID отеля']}" for info in hotel_info])
            return result
        elif response.status_code == 401:
            raise APIError('API Key is not authorized (Error 401)')
        else:
            raise ConnectionError
    except requests.ConnectionError:
        raise ConnectionError('Connection Error')

