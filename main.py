import requests
import os
from twilio.rest import Client
account_sid = "AC71623b20d70cb222a1cad05c946f582b"
auth_token = "df3a8a3c976e1359f58565601dcbb324"



#https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
#api.openweathermap.org/data/2.5/forecast?
weather_params={
    "appid": "aef2497e309c8f4adccf1751daeef7cd",
    "lat": -36.735691,
    "lon": 174.734173,
    #"exclude": "current, minutely, daily"
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast?", params=weather_params)
data = response.json()

# for i in range(0,12):
#     print(data["list"][i]["weather"][0]["id"])
w_slice = data["list"][:12]
will_rain = False

#print(w_slice)
for i in w_slice:
    print(i["weather"][0]["id"])
    if i["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Will rain, bring umbrella",
        from_="+14194064472",
        to="+64210565180"
    )
    print(message.sid)
