import os

from dotenv import load_dotenv


load_dotenv(verbose=True)

OPEN_WEATHER_MAP_API_KEY = os.environ.get("OPEN_WEATHER_MAP_API_KEY")
