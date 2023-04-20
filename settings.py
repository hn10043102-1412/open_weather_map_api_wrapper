import os

from dotenv import load_dotenv

load_dotenv(verbose=True)

API_KEY = os.environ.get("OPEN_WEATHER_API_KEY")
