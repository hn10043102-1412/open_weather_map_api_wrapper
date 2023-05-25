import data
from core import fetch


class AbstractWeatherAPI:
    def get_weather_data(self, area: data.Area) -> data.WeatherData:
        pass


class OpenWeatherAPI(AbstractWeatherAPI):
    """OpenWeatherAPI"""

    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_geo_data(self, city_name: str, state_code: str = "", country_code: str = "", limit: int = 1) -> data.GeoData:
        """名前から経度と緯度を取得する"""

        url = f"https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={limit}&appid={self.api_key}"
        response = fetch(url)
        fetch_data = response.json()
        return data.GeoData(fetch_data[0])

    def get_weather_data(self, area: data.Area, exclude: list[str] = None) -> data.WeatherData:
        """1回のリクエストでさまざまな情報を取得するAPI"""
        lat = area.geo_data.lat
        lon = area.geo_data.lon

        if exclude:
            part = ",".join(exclude)
        else:
            part = ""

        url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={self.api_key}"
        response = fetch(url)
        fetch_data = response.json()

        return data.WeatherData(fetch_data)

    def get_current_weather_data(self, area: data.Area) -> data.CurrentWeatherData:
        """現在の天気情報を取得するAPI"""

        lat = area.geo_data.lat
        lon = area.geo_data.lon
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.api_key}"
        response = fetch(url)
        fetch_data = response.json()

        return data.CurrentWeatherData(fetch_data)

    def get_forecast3h5d_weather_data(self, area: data.Area) -> data.Forecast3h5dWeatherData:
        """5日間で3時間ごとの天気情報を取得するAPI"""
        lat = area.geo_data.lat
        lon = area.geo_data.lon
        url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={self.api_key}"
        response = fetch(url)
        fetch_data = response.json()

        return data.Forecast3h5dWeatherData(fetch_data)
