import requests
from config_data.config import API_KEY
from loader import bot


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

def city_info(name_city):
    url = "https://hotels4.p.rapidapi.com/locations/v3/search"
    querystring = {"q": name_city, "locale": "en_US", "langid": '1033', "siteid": '300000001'}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }
    try:
        response = requests.get(url, params=querystring, headers=headers, timeout=10)
        if response.status_code == requests.codes.ok:
            full_names = [item['regionNames']['fullName'] for item in response.json()['sr']]
            gaia_id = response.json().get('sr', [])[0]['gaiaId']
            if not full_names:
                return None
            else:
                return full_names
        elif response.status_code == 401:
            raise APIError('API Key is not authorized (Error 401)')
        else:
            raise ConnectionError
    except requests.ConnectionError:
        raise ConnectionError('Connection Error')

#
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
