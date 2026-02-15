import requests
import logging
from config import Config

logger = logging.getLogger(__name__)

class WeatherService:
    def get_current_weather(self, city: str) -> dict:
        # 1. Check Offline Mode
        if Config.OFFLINE_MODE:
            return self._get_default_weather(city, is_mock=True)

        # 2. Check API Key
        api_key = Config.WEATHER_API_KEY
        base_url = Config.WEATHER_URL
        
        if not api_key:
            return self._get_default_weather(city, error="Missing API Key")

        # 3. Fetch Live Data
        try:
            params = {
                "q": city,
                "appid": api_key,
                "units": "metric"
            }
            response = requests.get(base_url, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()

            return {
                "temp": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "condition": data["weather"][0]["main"],
                "description": data["weather"][0]["description"],
                "wind_speed": data["wind"]["speed"],
                "city": data["name"],
                "is_mock": False
            }
        except Exception as e:
            logger.error(f"Weather API Error: {e}")
            return self._get_default_weather(city, error=str(e))

    def _get_default_weather(self, city="Unknown", is_mock=True, error=None):
        return {
            "temp": 24,
            "humidity": 55,
            "condition": "Clear",
            "description": "Sunny (Simulated)",
            "wind_speed": 12,
            "city": city if city else "Demo City",
            "is_mock": is_mock,
            "error": error
        }