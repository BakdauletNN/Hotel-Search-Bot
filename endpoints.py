

#locations/v3/search
#
# import requests
# import json
# url = "https://hotels4.p.rapidapi.com/locations/v3/search"
#
# querystring = {"q":"new-york","locale":"en_US","langid":"1033","siteid":"300000001"}
#
# headers = {
# 	"X-RapidAPI-Key": ""
# 	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
# json_file = response.json()
# result = json.dumps(json_file,indent=4)
# print(result)


#
#
# #properties/v2/list
#
# import requests
# import json
#
#
# url = "https://hotels4.p.rapidapi.com/properties/v2/list"
#
# payload = {
# 	"currency": "USD",
# 	"eapid": 1,
# 	"locale": "en_US",
# 	"siteId": 300000001,
# 	"destination": { "regionId": "553248629421290266" },
# 	"checkInDate": {
# 		"day": 10,
# 		"month": 10,
# 		"year": 2022
# 	},
# 	"checkOutDate": {
# 		"day": 15,
# 		"month": 10,
# 		"year": 2022
# 	},
# 	"rooms": [
# 		{
# 			"adults": 2,
# 			"children": [{ "age": 5 }, { "age": 7 }]
# 		}
# 	],
# 	"resultsStartingIndex": 0,
# 	"resultsSize": 200,
# 	"sort": "PRICE_LOW_TO_HIGH",
# 	"filters": { "price": {
# 			"max": 150,
# 			"min": 100
# 		} }
# }
# headers = {
# 	"content-type": "application/json",
# 	"X-RapidAPI-Key": "",
# 	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
# }
#
# response = requests.post(url, json=payload, headers=headers)
# json_file = response.json()
# result = json.dumps(json_file,indent=4)
# print(result)
# #
#






# # #properties/v2/detail
# #
# import requests
# import json
#
#
# url = "https://hotels4.p.rapidapi.com/properties/v2/detail"
#
# payload = {
# 	"currency": "USD",
# 	"eapid": 1,
# 	"locale": "en_US",
# 	"siteId": 300000001,	"propertyId": "9209612"
# }
# headers = {
# 	"content-type": "application/json",
# 	"X-RapidAPI-Key": "",
# 	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
# }
#
# response = requests.post(url, json=payload, headers=headers)
# json_file = response.json()
# result = json.dumps(json_file,indent=4)
# print(result)






#hotel photos

# import requests
#
# url = "https://hotels4.p.rapidapi.com/properties/get-hotel-photos"
#
# querystring = {"id":"1178275040"}
#
# headers = {
# 	"X-RapidAPI-Key": "",
# 	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.json())