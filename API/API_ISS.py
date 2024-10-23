import requests
from datetime import datetime
import smtplib
import pytz
import time
from env import BUISNES_EMAIL, OPEN_PASSWORD, MY_EMAIL

MY_LAT = 1.7075  # Your latitude
MY_LONG = 2.215  # Your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()


    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(f"latitude: {iss_latitude}, longitude: {iss_longitude}")

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_str = data["results"]["sunrise"]
    sunset_str = data["results"]["sunset"]

    sunrise = datetime.fromisoformat(sunrise_str).replace(tzinfo=pytz.utc)
    sunset = datetime.fromisoformat(sunset_str).replace(tzinfo=pytz.utc)
    print(f"this is the sunset time: {sunset}, this is the sunrise time: {sunrise}")

    # Localize time_now to UTC timezone
    time_now = datetime.now(pytz.utc)

    if time_now >= sunset or time_now <= sunrise:
        return True



while True:
    time.sleep(10)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(BUISNES_EMAIL, OPEN_PASSWORD)
        connection.sendmail(from_addr=BUISNES_EMAIL, to_addrs=MY_EMAIL,
                            msg='Subject: Look Up \n\nThe ISS is overhead!')
        connection.close()
