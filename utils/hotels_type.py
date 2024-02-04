from loguru import logger
from config_data.config import API_KEY
import requests
from handlers.custom_handlers.adults import adults
from handlers.custom_handlers.children import age_children
from handlers.custom_handlers.entry_data import entry_date
from handlers.custom_handlers.date_exit import exit_date
from handlers.custom_handlers.callback_data import handle_location_callback
from loader import bot


api = {'X-RapidApi-Key': API_KEY, 'X-RapidAPI-Host': "hotels4.p.rapidapi.com"}


@logger.catch()
def request_api(url, params, headers):
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        if response.status_code == requests.codes.ok:
            return response
        else:
            raise ConnectionError
    except requests.ConnectionError:
        print('Error')


class APIError(Exception):
    pass


@logger.catch()
@bot.message_handler()
def get_date(adults_amount=adults, child_age=age_children,
             # entry_day=check_in_day, entry_month=check_in_month, entry_year=check_in_year,
             # exit_day=check_out_day, exit_month=check_out_month, exit_year=check_out_year,
             id=handle_location_callback) -> None:
    entry_day, entry_month, entry_year = map(int, entry_date.split('.'))
    exit_day, exit_month,  exit_year = map(int, exit_date.split('.'))

    url = "https://hotels4.p.rapidapi.com/properties/v2/list"
    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "destination": {"regionId": id},
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
                "adults": adults_amount,
                "children": [{"age": child_age}, {"age": child_age}]
            }
        ],
        "resultsStartingIndex": 0,
        "resultsSize": 10,
        "sort": "PRICE_LOW_TO_HIGH",
        "filters": {"price": {
            "max": 150,
            "min": 100
        }}
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
            return properties
            for i, property_data in enumerate(properties[:5]):
                    hotel_name = properties[i]["name"]
                    hotel_id = properties[i]['id']
                    bot.send_message(message)
                    print(f"Отель {i + 1}:")
                    print("Имя отеля:", hotel_name)
                    print("ID отеля:", hotel_id)
                    print("-" * 10)

        elif response.status_code == 401:
            raise APIError('API Key is not authorized (Error 401)')
        else:
            raise ConnectionError
    except requests.ConnectionError:
        raise ConnectionError('Connection Error')


