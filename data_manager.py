import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.url = "https://api.sheety.co/34e1d9e5dd6801763233a58d7f5ebe37/flightDeals/prices"

    def get_sheet_data(self):
        sheet_data = requests.get(self.url)
        print(sheet_data.json())
