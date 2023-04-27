import settings
import data
import core


class GeoCogingAPI:
    """地理情報API"""

    @classmethod
    def get_geo_data(self, city_name: str, state_code="", country_code="", limit=1):
        """名前から経度と緯度を取得する"""

        url = f"https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={limit}&appid={settings.API_KEY}"
        response = core.fetch(url)
        fetch_data = response.json()
        return data.GeoData(fetch_data[0])


class AbstractWeatherAPI:
    @classmethod
    def get_weather_data(self, area: data.Area):
        return NotImplementedError()


class OneCallAPI(AbstractWeatherAPI):
    """1リクエストで多数の情報を取得するAPI"""

    @classmethod
    def get_weather_data(self, area: data.Area, exclude = None) -> data.WeatherData:
        lat = area.geo_data.lat
        lon = area.geo_data.lon

        if exclude:
            part = ",".join(exclude)
        else:
            part = ""

        url =f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={settings.API_KEY}"
        response = core.fetch(url)
        data = response.json()
        return data.WeatherData(data)


class CurrentWeatherAPI(AbstractWeatherAPI):
    """現在の天気情報を取得するAPI"""

    @classmethod
    def get_weather_data(self, area: data.Area):
        lat = area.geo_data.lat
        lon = area.geo_data.lon
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={settings.API_KEY}"
        response = core.fetch(url)
        fetch_data = response.json()
        return data.CurrentWeatherData(fetch_data)


class Forecast3h5dWeatherAPI(AbstractWeatherAPI):
    @classmethod
    def get_weather_data(self, area: data.Area):
        lat = area.geo_data.lat
        lon = area.geo_data.lon
        url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={settings.API_KEY}"
        response = core.fetch(url)
        fetch_data = response.json()
        return data.Forecast3h5dWeatherData(fetch_data)
