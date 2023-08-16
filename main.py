import requests
from datetime import datetime

MY_LAT = 44.426765  # Your latitude
MY_LONG = 26.102537  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.
is_close = False
if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and \
        MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
    is_close = True

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

hour_now = datetime.now().hour

is_night = False
if hour_now >= sunset or hour_now <= sunrise:
    is_night = True

if is_close and is_night:
    # Send email placeholder
    print("Look up ISS is close")
