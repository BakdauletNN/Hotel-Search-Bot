from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def create_city_keyboard(city_names):
    keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [InlineKeyboardButton(city, callback_data=city) for city in city_names]
    keyboard.add(*buttons)
    return keyboard


import requests

url = "https://hotels4.p.rapidapi.com/locations/v3/search"

querystring = {"q":"new york","locale":"en_US","langid":"1033","siteid":"300000001"}

headers = {
	"X-RapidAPI-Key": "21b1f0d5f0msh794c4bc1f79575bp1c2869jsnd0012662ca39",
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())