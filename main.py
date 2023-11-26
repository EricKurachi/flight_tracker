#This file will need to use the FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

sheet = DataManager()
sheet_data = sheet.get_sheet_data()

flight_search = FlightSearch()

for row in sheet_data["prices"]:
    if not row["iataCode"]:
        row["iataCode"] = flight_search.check_iata_code(row["city"])

sheet.update_destination_codes()

