import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ENV = os.getenv("ENV", "development")
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
    # Default to OpenWeatherMap if not set, but prioritize the ENV var
    WEATHER_URL = os.getenv("WEATHER_URL", "https://api.openweathermap.org/data/2.5/weather")
    FIREBASE_CREDENTIALS_PATH = os.getenv("FIREBASE_CREDENTIALS_PATH")
    OFFLINE_MODE = os.getenv("OFFLINE_MODE", "false").lower() == "true"