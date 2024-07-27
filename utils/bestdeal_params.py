import re
from loguru import logger
from config_data.config import API_KEY
import requests


api = {'X-RapidApi-Key': API_KEY, 'X-RapidAPI-Host': "hotels4.p.rapidapi.com"}


class APIError(Exception):
    pass


def km_to_miles(km):  # функция для того чтобы конвертировать км в мили для сравнения с данными из API
    return km / 1.60934


@logger.catch()
def get_data_bestdeal(data: dict):
    entry_date = data.get('entry')
    entry_day, entry_month, entry_year = map(int, entry_date.split('.'))

    exit_date = data.get('exit')
    exit_day, exit_month, exit_year = map(int, exit_date.split('.'))

    adults = data.get('adults')
    children_ages = data.get('child_age', [])
    hotels_amount_param = data.get('hotels_qty', 1)

    handle_location_callback = data.get('id_location')
    min_price = float(data.get('price_min_bestdeal'))
    max_price = float(data.get('price_max_bestdeal'))
    distance_param_km = data.get('center_distance')
    distance_param_mi = km_to_miles(distance_param_km)

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
        "sort": "DISTANCE",
        "filters": {
            "price": {
                "max": max_price,
                "min": min_price
            }
        }
    }
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "hotels4.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        json_data = response.json()
        properties = json_data.get("data", {}).get("propertySearch", {}).get("properties", [])
        hotel_info = []
        hotel_ids = []
        for i, property_data in enumerate(properties[:int(hotels_amount_param)]):
            one_day_price_str = property_data["price"]["options"][0]["formattedDisplayPrice"]
            one_day_price = float(re.sub(r'[^\d.]', '', one_day_price_str))
            distance_from_center = float(property_data["destinationInfo"]["distanceFromMessaging"].split(' ')[0])

            if distance_from_center <= distance_param_mi and min_price <= one_day_price <= max_price:
                hotel_name = property_data["name"]
                hotel_id = property_data['id']

                hotel_info.append({
                    "Отель": i + 1,
                    "Имя отеля": hotel_name,
                    "ID отеля": hotel_id,
                    "Цена за 1 сутки": one_day_price_str
                })
                hotel_ids.append(hotel_id)

        if not hotel_info:
            return "Нет отелей, соответствующих указанным критериям.", []

        result = "\n".join([
            f"Отель {info['Отель']}: {info['Имя отеля']}, ID: {info['ID отеля']}, Цена за 1 сутки: {info['Цена за 1 сутки']}"
            for info in hotel_info])
        return result, hotel_ids

    except requests.RequestException as err:
        logger.error(f"Error occurred: {err}")
        raise APIError('Request Error')
