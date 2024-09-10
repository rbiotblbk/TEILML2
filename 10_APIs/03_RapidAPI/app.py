import requests

url = "https://aerodatabox.p.rapidapi.com/flights/airports/iata/STR/2024-09-09T20:00/2024-09-10T08:00"

querystring = {"withLeg": "true", "direction": "Arrival", "withCancelled": "true",
               "withCodeshared": "true", "withCargo": "false", "withPrivate": "true", "withLocation": "false"}

headers = {
    "x-rapidapi-key": "57e40df905msh89f91a584028707p1724bfjsn063fbf3c8395",
    "x-rapidapi-host": "aerodatabox.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
