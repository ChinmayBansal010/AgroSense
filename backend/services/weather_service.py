
import requests
from config import WEATHER_API_KEY, WEATHER_URL, OFFLINE_MODE

def fetch_weather(city: str):
    if OFFLINE_MODE:
        return {"rainfall": 3, "temperature": 27, "humidity": 60}

    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }
    r = requests.get(WEATHER_URL, params=params)
    r.raise_for_status()
    data = r.json()["list"][0]

    return {
        "rainfall": data.get("rain", {}).get("3h", 0),
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"]
    }
