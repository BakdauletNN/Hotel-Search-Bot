from typing import Union, List, Dict
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


class APIError(Exception):
    pass


def city_info(name_city) -> Union[None, List[Dict[str, Union[str, int]]]]:
    url = "https://hotels4.p.rapidapi.com/locations/v3/search"
    querystring = {"q": name_city.strip(), "locale": "en_US", "langid": '1033', "siteid": '300000001'}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }
    try:
        response = requests.get(url, params=querystring, headers=headers, timeout=10)
        if response.status_code == requests.codes.ok:
            locations = response.json().get('sr', [])
            filtered_locations = [
                {"ID": item['gaiaId'], "name": item['regionNames']['fullName']}
                for item in locations
                if item['type'] in ['CITY', 'NEIGHBORHOOD']
            ]
            if not filtered_locations:
                return None
            else:
                return filtered_locations
        elif response.status_code == 401:
            raise APIError('API Key is not authorized (Error 401)')
        else:
            raise ConnectionError
    except requests.ConnectionError:
        raise ConnectionError('Connection Error')


# def main():
#     try:
#         result = city_info('tokyo')
#         print(result)
#         print()
#     except APIError as e:
#         print(f'API Error: {str(e)}')
#     except ConnectionError as e:
#         print(f'Connection Error: {str(e)}')
#
# main()
