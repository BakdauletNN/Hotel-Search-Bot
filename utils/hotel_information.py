from loguru import logger
import requests
from config_data.config import API_KEY

api = {'X-RapidApi-Key': API_KEY, 'X-RapidAPI-Host': "hotels4.p.rapidapi.com"}

def request_api(url, params, headers):
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        if response.status_code == requests.codes.ok:
            return response
        else:
            raise ConnectionError
    except requests.ConnectionError:
        print('Error')

@logger.catch()
def hotel_info(data: dict):
    id_hotel = data.get('id_hotel')  # Получаем идентификатор отеля из словаря
    url = "https://hotels4.p.rapidapi.com/properties/v2/detail"

    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "propertyId": id_hotel  # Используем идентификатор отеля
    }
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "hotels4.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    try:
        if response.status_code == requests.codes.ok:
            json_data = response.json()
            properties = json_data.get("data", {}).get("propertyInfo", {})
            # Обработка данных отеля здесь
            name = properties.get('summary', {}).get('name', "")
            location = properties.get("summary", {}).get("location", {}).get("address", {}).get("addressLine", "")
            map_url = properties.get("summary", {}).get("location", {}).get("staticImage", {}).get("url", "")



        else:
            raise ConnectionError
    except requests.ConnectionError:
        raise ConnectionError('Connection Error')
