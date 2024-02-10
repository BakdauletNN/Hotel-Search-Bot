from loguru import logger
from config_data.config import API_KEY
import requests
from handlers.custom_handlers.adults import adults
from handlers.custom_handlers.children import age_children
from handlers.custom_handlers.entry_data import entry_date
from handlers.custom_handlers.date_exit import exit_date
from handlers.custom_handlers.callback_data import handle_location_callback
from datetime import datetime


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
def get_date(adults_amount=adults, child_age=age_children,
             id=handle_location_callback) -> None:
    entry_configs = datetime.strptime(entry_date, '%d.%m.%Y')
    exit_configs = datetime.strptime(exit_date, '%d.%m.%Y')

    # Получение отдельных частей даты въезда
    entry_day = entry_configs.day
    entry_month = entry_configs.month
    entry_year = entry_configs.year

    # Получение отдельных частей даты выезда
    exit_day = exit_configs.day
    exit_month = exit_configs.month
    exit_year = exit_configs.year

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
            for i, property_data in enumerate(properties[:5]):
                hotel_name = properties[i]["name"]
                hotel_id = properties[i]['id']
                return f"Отель {i + 1}:"
                return "Имя отеля:", hotel_name
                return "ID отеля:", hotel_id

        elif response.status_code == 401:
            raise APIError('API Key is not authorized (Error 401)')
        else:
            raise ConnectionError
    except requests.ConnectionError:
        raise ConnectionError('Connection Error')


