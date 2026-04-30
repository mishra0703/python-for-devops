import requests
import json
from datetime import datetime

params = {
  'access_key': '3b3cf8b1314dcd8a8674b94072db63cc'
}

api_result = requests.get('https://api.aviationstack.com/v1/flights', params)

api_response = api_result.json()



def print_flight_details():     
    flight_details = {}

    Total_Flight_Details = int(input("Enter how many flight details you want (out of 100): "))
    index=1

    for flight in api_response["data"]:    
        if index > Total_Flight_Details:
            break

        if (flight['live'] != "None"):
            flight_details[f"Flight_{index}"] = {
                "flight_number"      : flight['flight']['iata'],
                "airline"            : flight['airline']['name'],
                "departure_airport"  : flight['departure']['airport'],
                "departure_iata"     : flight['departure']['iata'],
                "arrival_airport"    : flight['arrival']['airport'],
                "arrival_iata"       : flight['arrival']['iata'],
                "scheduled"          : datetime.fromisoformat(flight['departure']['scheduled']).strftime("%B %d, %Y at %I:%M %p UTC"),
                "terminal"           : flight['departure']['terminal'],
                "gate"               : flight['departure']['gate']
            }
            index+=1    

    print(flight_details)
    with open("Flight_Details.json","w+") as json_file:
        json.dump(flight_details,json_file)
   

print_flight_details()