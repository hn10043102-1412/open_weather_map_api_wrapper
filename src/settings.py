import os

from dotenv import load_dotenv


# .envファイルを読み込み、環境変数にセットする
load_dotenv(verbose=True)

OPEN_WEATHER_MAP_API_KEY = os.environ.get("OPEN_WEATHER_MAP_API_KEY")
