import requests

TEQUILA_URL = "https://api.tequila.kiwi.com/locations/query"
TEQUILA_KEY = "Az-_OKn4Zs5eU6xGF2sG3It7QP3p3rDi"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.locations_params = None
        self.location_header = {
            "apikey": TEQUILA_KEY
        }

    def check_iata_code(self, city):
        query = {
            "term": city,
            "location_types": "city"
        }

        location_response = requests.get(TEQUILA_URL, params=query, headers=self.location_header)
        iata_code = location_response.json()['locations'][0]['code']
        return iata_code
