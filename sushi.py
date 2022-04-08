import requests
import schedule
import time
import os
from twilio.rest import Client

def job():
    
    aSID = os.environ["TWILIO_ACCOUNT_SID"]
    authToken = os.environ["TWILIO_AUTH_TOKEN"]

    sushi = ""
    response = requests.get("https://michigan-dining-api.tendiesti.me/v1/items")
    response = response.json()
    for key,val in response["items"].items():
        if key == "sushi boss sampler":
            for keyd, vald in val["diningHallMatches"].items():
                sushi = sushi + "Dining Hall: " + keyd, "   Date: " + list(vald["mealTimes"])[0] + "\n"
    
    client = Client(aSID, authToken)

    client.messages.create(
        to=os.environ["MY_PHONE_NUMBER"],
        from_="+17163254250",
        body=sushi
    )


schedule.every().sunday.at("12:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)