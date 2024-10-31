from loguru import logger
from config_data.config import API_KEY
import requests
import re


api = {'X-RapidApi-Key': API_KEY, 'X-RapidAPI-Host': "hotels4.p.rapidapi.com"}


class APIError(Exception):
    pass


def km_to_miles(km):
    return km / 1.60934


@logger.catch()
def get_data(data: dict, sort_type: str, filters: dict = None):
    entry_date = data.get('entry')
    exit_date = data.get('exit')

    if not entry_date or not exit_date:
        logger.error("There are no entry or exit dates")
        return None, []

    entry_day, entry_month, entry_year = map(int, entry_date.split('.'))
    exit_day, exit_month, exit_year = map(int, exit_date.split('.'))

    adults = data.get('adults')
    children_ages = data.get('child_age', [])
    hotels_amount_param = data.get('hotels_qty', 1)
    hotels_amount_param = int(hotels_amount_param)
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
        "sort": sort_type,
        "filters": filters if filters else {}
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

        if not json_data or "data" not in json_data:
            logger.error("Failed to retrieve data from API. Answer: %s", json_data)
            return None, []

        properties = json_data.get("data", {}).get("propertySearch", {}).get("properties", [])
        if not properties:
            logger.warning("No hotels found matching your request")
            return None, []

        hotel_info = []
        hotel_ids = []
        min_price = float(filters.get("price", {}).get("min")) if filters and filters.get("price", {}).get("min") else None
        max_price = float(filters.get("price", {}).get("max")) if filters and filters.get("price", {}).get("max") else None
        distance_param_km = data.get('center_distance')
        distance_param_mi = km_to_miles(distance_param_km) if distance_param_km else None

        for property_data in properties:
            price_options = property_data.get("price", {}).get("options", [])
            if not price_options:
                continue

            one_day_price_str = price_options[0].get("formattedDisplayPrice", "N/A")
            one_day_price = float(re.sub(r'[^\d.]', '', one_day_price_str)) if one_day_price_str != "N/A" else None
            distance_from_center_str = property_data.get("destinationInfo", {}).get("distanceFromMessaging")
            if distance_from_center_str:
                match = re.search(r'\d+(\.\d+)?', distance_from_center_str)
                distance_from_center = float(match.group(0)) if match else None
            else:
                distance_from_center = None

            if ((distance_param_mi is None or (
                    distance_from_center is not None and distance_from_center <= distance_param_mi)) and
                    (min_price is None or (one_day_price is not None and one_day_price >= min_price)) and
                    (max_price is None or (one_day_price is not None and one_day_price <= max_price))):
                hotel_name = property_data["name"]
                hotel_id = property_data['id']

                hotel_info.append({
                    "Hotel name": hotel_name,
                    "ID Hotel": hotel_id,
                    "Price for 1 day": one_day_price_str,
                    "Price": one_day_price
                })
                hotel_ids.append(hotel_id)

        sort_reverse = (sort_type == "PROPERTY_CLASS")
        hotel_info = [info for info in hotel_info if 'Price' in info]

        if not hotel_info:
            return None, []

        hotel_info.sort(key=lambda x: x["Price"], reverse=sort_reverse)

        hotel_info = hotel_info[:hotels_amount_param]

        if not hotel_info:
            return None, []

        result = "\n".join([
            f"Hotel {i + 1}: {info['Hotel name']}, ID: {info['ID Hotel']}, Price for 1 day: {info['Price for 1 day']}"
            for i, info in enumerate(hotel_info)
        ])

        return result, hotel_ids[:hotels_amount_param]

    except requests.RequestException as err:
        logger.error(f"Error when requesting to API: {err}")
        return None, []
