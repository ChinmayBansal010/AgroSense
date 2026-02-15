
import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("ENV", "development")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_URL = os.getenv("WEATHER_URL")
FIREBASE_CREDENTIALS_PATH = os.getenv("FIREBASE_CREDENTIALS_PATH")
OFFLINE_MODE = os.getenv("OFFLINE_MODE", "false").lower() == "true"
