import requests
import json
import os
import re


api = {'X-RapidApi-Key': os.getenv('API_KEY'), 'X-RapidAPI-Host': "hotels4.p.rapidapi.com"}


def request_api(url, params, headers):
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        if response.status_code == requests.codes.ok:
            return response
        else:
            raise ConnectionError

    except requests.ConnectionError:
        print('Error')



async def city_info(name_city):
    url = "https://hotels4.p.rapidapi.com/locations/v3/search"
    querystring = {"q": name_city, "locale": "en_US", "langid": '1033', "siteid": '300000001'}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": os.getenv('API_KEY'),
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }
    try:
        response = requests.get(url, params=querystring, headers=headers,timeout=10)
        if response.status_code == requests.codes.ok:
            full_names = [item['regionNames']['fullName'] for item in response.json()['sr']]
            print(full_names)
        else:
            raise ConnectionError
    except requests.ConnectionError:
        print('Error')

