from loguru import logger
from config_data.config import API_KEY
import requests


api = {'X-RapidApi-Key': API_KEY, 'X-RapidAPI-Host': "hotels4.p.rapidapi.com"}


class APIError(Exception):
    pass


@logger.catch()
def get_data(data: dict):
    entry_date = data.get('entry')
    entry_day, entry_month, entry_year = map(int, entry_date.split('.'))

    exit_date = data.get('exit')
    exit_day, exit_month, exit_year = map(int, exit_date.split('.'))

    adults = data.get('adults')
    children_ages = data.get('child_age', [])

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
                "children": [{"age": age} for age in children_ages] if children_ages else []
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
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == requests.codes.ok:
            json_data = response.json()
            properties = json_data.get("data", {}).get("propertySearch", {}).get("properties", [])
            hotel_info = []
            hotel_ids = []
            for i, property_data in enumerate(properties[:5]):
                hotel_name = property_data["name"]
                hotel_id = property_data['id']
                hotel_info.append({
                    "Отель": i + 1,
                    "Имя отеля": hotel_name,
                    "ID отеля": hotel_id
                })
                hotel_ids.append(hotel_id)  # Добавляем id отеля в список

            result = "\n".join([f"Отель {info['Отель']}: {info['Имя отеля']}, ID: {info['ID отеля']}" for info in hotel_info])
            return result, hotel_ids  # Возвращаем результат и список идентификаторов
        elif response.status_code == 401:
            raise APIError('API Key is not authorized (Error 401)')
        else:
            raise ConnectionError
    except requests.ConnectionError:
        raise ConnectionError('Connection Error')
