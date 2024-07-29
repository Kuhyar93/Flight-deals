# from flight_data import FlightData
# from data_manager import DataManager
#
#
# data_manager = DataManager()
# sheet_data = data_manager.get_destination_data()
# flight_data = FlightData(sheet_data)
# flight_data.print_cheapest_flight_for_each_city()






# if sheet_data[0]["iataCode"] == "":
#     from flight_search import FlightSearch
#     flight_search = FlightSearch()
#     for row in sheet_data:
#         row["iataCode"] = flight_search.get_destination_code(row["city"])
#     print(f"sheet_data:\n {sheet_data}")
#
#     data_manager.destination_data = sheet_data
#     data_manager.update_destination_codes()
#

# TEQUILA SHIT



#
# TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
# TEQUILA_API_KEY = "msAJ06QhGFU6YWl1ya2DEEYTuTwLq1ol"
# header = {"apikey": TEQUILA_API_KEY}
# code_search_para = {
#     "fly_from": "LON",
#     "fly_to": "SYD",
#     "date_from": (dt.now() + timedelta(days=1)).strftime("%d/%m/%Y"),
#     "date_to": (dt.now() + timedelta(days=180)).strftime("%d/%m/%Y"),
#     "nights_in_dst_from": 7,
#     "nights_in_dst_to": 28,
#     "one for city": 1,
#     "curr": "GBP"
# }
#
# for i in range(len(sheet_data)):
#     iata = sheet_data[i]["iataCode"]
#     code_search_para["fly_to"] = iata
#     response = requests.get(url=TEQUILA_ENDPOINT, headers=header, params=code_search_para)
#     response.raise_for_status()
#     flight_price = response.json()["data"][0]['price']
#     print(f"{sheet_data[i]['city']}: £{flight_price}")













# for row in flight_data:
#     print(row['price'])
#



#print(sheet_data)


# with open("csv_data.txt", mode='w') as data:
#     for data_row in sheet_data:
#         data.write(json.dumps(data_row))
#
#
#

#
# sheet_data = []
# with open("csv_data.txt", mode="r") as data:
#     for line in data:
#         sheet_data.append(line)

import requests

# from datetime import datetime, timedelta
# from data_manager import DataManager
# from flight_search import FlightSearch
# # from notification_manager import NotificationManager
#
# ORIGIN_CITY_IATA = "LON"
#
# data_manager = DataManager()
# flight_search = FlightSearch()
# # notification_manager = NotificationManager()
#
# sheet_data = data_manager.get_destination_data()
#
# if sheet_data[0]["iataCode"] == "":
#     city_names = [row["city"] for row in sheet_data]
#     print(city_names)
#     codes = flight_search.get_destination_codes(city_names)
#     data_manager.update_destination_codes(codes)
#     sheet_data = data_manager.get_destination_data()
#
# today = datetime.now() + timedelta(1)
# six_month_from_today = datetime.now() + timedelta(6 * 30)
#
# for destination in sheet_data:
#     flight = flight_search.check_flights(
#         ORIGIN_CITY_IATA,
#         destination["iataCode"],
#         from_time=today,
#         to_time=six_month_from_today
#     )
#
#     if flight.price < destination["lowestPrice"]:
#         # notification_manager.send_sms(
#         #     message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
#         # )
#         print(f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}.")












SHEETY_USERS_ENDPOINT = "https://api.sheety.co/9e22f5da28ceec3ed357e51ca1152d65/flightDeals/users"

def add_users_to_club():
    print("Welcome to Kuhyar's Flight club.")
    print("We find you the best flight deals and email you.")
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    email = input("What is your Email? ")
    email_again = input("Type your email again. ")
    if email.lower() == email_again.lower():
        new_data = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
            }
        }
        response = requests.post(url=SHEETY_USERS_ENDPOINT,
                                 json=new_data)
        response.raise_for_status()
        print(response.json())


add_users_to_club()





