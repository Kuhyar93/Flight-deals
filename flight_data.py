# import requests
# ORIGIN_CITY_IATA = "LON"
# from datetime import datetime as dt
# from datetime import timedelta
#
# TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
# TEQUILA_API_KEY = "msAJ06QhGFU6YWl1ya2DEEYTuTwLq1ol"
# TOMORROW_DATE = (dt.now() + timedelta(days=1)).strftime("%d/%m/%Y")
# SIX_MONTH_FROM_NOW = (dt.now() + timedelta(days=180)).strftime("%d/%m/%Y")
# CURRENCY = "GBP"
# class FlightData:
#     def __init__(self, sheet_data):
#         self.sheet_data = sheet_data
#
#
#
#     def print_cheapest_flight_for_each_city(self):
#         header = {"apikey": TEQUILA_API_KEY}
#         code_search_para = {
#             "fly_from": ORIGIN_CITY_IATA,
#             "fly_to": "",
#             "date_from": TOMORROW_DATE,
#             "date_to": SIX_MONTH_FROM_NOW,
#             "nights_in_dst_from": 7,
#             "nights_in_dst_to": 28,
#             "flight_type": "round",
#             "one for city": 1,
#             "max_stopovers": 0,
#             "curr": CURRENCY
#         }
#         for i in range(len(self.sheet_data)):
#             destination_iata = self.sheet_data[i]["iataCode"]
#             code_search_para["fly_to"] = destination_iata
#             response = requests.get(url=TEQUILA_ENDPOINT, headers=header, params=code_search_para)
#             response.raise_for_status()
#             flight_price = response.json()["data"][0]['price']
#             if flight_price < self.sheet_data[i]['lowestPrice']:
#                 print(f"Low price alert. Only £{flight_price} to fly from {ORIGIN_CITY_IATA} to {destination_iata}")
#
#             #print(f"{self.sheet_data[i]['city']}: £{flight_price}")
#
#
#
#
#

class FlightData:

    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
