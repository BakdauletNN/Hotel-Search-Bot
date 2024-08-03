from loguru import logger
import requests
from config_data.config import API_KEY


api = {'X-RapidApi-Key': API_KEY, 'X-RapidAPI-Host': "hotels4.p.rapidapi.com"}


@logger.catch()
def hotel_info(data: dict):
    id_hotel = data.get('property_id')
    photos_amount_user = data.get('photos', 0)
    url = "https://hotels4.p.rapidapi.com/properties/v2/get-summary"
    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "propertyId": id_hotel
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
        properties = json_data.get("data", {}).get("propertyInfo", {})

        if not properties:
            logger.error(f"Информации по id не найдено: {id_hotel}")
            return None

        name = properties.get('summary', {}).get('name', "")
        location = properties.get("summary", {}).get("location", {}).get("address", {}).get("addressLine", "")
        map_url = properties.get("summary", {}).get("location", {}).get("staticImage", {}).get("url", "")
        photos = properties.get('propertyGallery', {}).get('images', [])[:int(photos_amount_user)]

        photo_urls = [photo.get('image', {}).get('url', '') for photo in photos]

        hotel_info_str = f"Name hotel: {name}\nLocation: {location}\nMap url: {map_url}"
        return hotel_info_str, photo_urls

    except requests.RequestException as err:
        logger.error(f"Ошибка запроса: {err}")
        return None
