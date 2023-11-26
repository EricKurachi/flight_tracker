#This file will need to use the FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager

import requests
sheet = DataManager()

#sheet.get_sheet_data()

location_url = "https://api.tequila.kiwi.com/locations/query"

location_header = {
    "apikey": "Az-_OKn4Zs5eU6xGF2sG3It7QP3p3rDi"
}

locations_params = {
    "term": "Campinas",
    "locale": "pt-BR",
    "limit": 1
}

location_response = requests.get(location_url, locations_params, headers=location_header)

print(location_response.json()['locations'][0]['id'])