import os
from loader import bot
from config_data.config import API_KEY
import requests
from handlers.custom_handlers.adults import adults
from handlers.custom_handlers.children import child,age_children
from handlers.custom_handlers.entry_data import entry_date
from handlers.custom_handlers.date_exit import exit_date
from handlers.custom_handlers.callback_data import handle_location_callback
from handlers.custom_handlers.amount_hotel import amount_hotel


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


check_in_day, check_in_month, check_in_year = map(int, entry_date.split('.'))
check_out_day, check_out_month, check_out_year = map(int, exit_date.split('.'))


def get_date(adults_amount=adults, children_amount=child, child_age=age_children,
             entry_day=check_in_day, entry_month=check_in_month, entry_year=check_in_year,
             exit_day=check_out_day, exit_month=check_out_month, exit_year=check_out_year,
             id=handle_location_callback, amount_hotels=amount_hotel):

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
        "resultsSize": 200,
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
