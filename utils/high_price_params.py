from loguru import logger
from config_data.config import API_KEY
import requests


api = {'X-RapidApi-Key': API_KEY, 'X-RapidAPI-Host': "hotels4.p.rapidapi.com"}


class APIError(Exception):
    pass

@logger.catch()
def get_high_price_data(data: dict):
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
        "sort": "REVIEW",
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        json_data = response.json()
        properties = json_data.get("data", {}).get("propertySearch", {}).get("properties", [])
        hotel_info = []
        hotel_ids = []
        for i, property_data in enumerate(properties[:5]):
            hotel_name = property_data["name"]
            hotel_id = property_data['id']
            one_day_price = property_data["price"]["options"][0]["formattedDisplayPrice"]

            hotel_info.append({
                "Отель": i + 1,
                "Имя отеля": hotel_name,
                "ID отеля": hotel_id,
                "Цена за 1 сутки": one_day_price
            })
            hotel_ids.append(hotel_id)

        result = "\n".join([f"Отель {info['Отель']}: {info['Имя отеля']}, ID: {info['ID отеля']}, Цена за 1 сутки: {info['Цена за 1 сутки']}" for info in hotel_info])
        return result, hotel_ids

    except requests.RequestException as err:
        logger.error(f"Error occurred: {err}")
        raise APIError('Request Error')
