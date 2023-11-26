import requests

SHEETY_URL = "https://api.sheety.co/34e1d9e5dd6801763233a58d7f5ebe37/flightDeals/prices"
SHEETY_TOKEN = "345yyvErt6y6fh545y4Gh465j76gdfgdJOLKS"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_data = {}
        self.header = {
            "Autorization": SHEETY_TOKEN
        }

    def get_sheet_data(self):
        # Get data from Google Sheets
        response = requests.get(url=SHEETY_URL, headers=self.header)
        self.sheet_data = response.json()
        # print(self.sheet_data)
        return self.sheet_data

    def update_destination_codes(self):
        for city in self.sheet_data["prices"]:
            params = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            requests.put(f"{SHEETY_URL}/{city["id"]}", json=params, headers=self.header)
