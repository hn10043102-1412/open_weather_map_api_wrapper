import settings

import requests


class HTTPRequestError(Exception):
    pass


class CheckPriceError(HTTPRequestError):
    pass


def fetch(url: str, params = None):
    """HTTPリクエストを行う"""

    response = requests.get(url, params)
    if response.status_code != 200:
        raise CheckPriceError(response)

    return response


class GeoData:
    def __init__(self, data: dict) -> None:
        self.data = data
        self.name = data.get("name")
        self.lat = data.get("lat")
        self.lon = data.get("lon")


def geo_coding_api(city_name: str, state_code="", country_code="", limit=1):
    """名前から経度と緯度を取得する"""

    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={limit}&appid={settings.API_KEY}"
    response = fetch(url)
    data = response.json()
    return GeoData(data[0])


class WeatherData:
    """天気モデル"""

    class Current:
        """現在の天気モデル"""

        def __init__(self, data):
            self.data = data
            self.dt = data.get("dt")
            self.temp = data.get("temp")
            self.feels_like = data.get("feels_like")
            self.pressure = data.get("pressure")
            self.humidity = data.get("humidity")
            self.clouds = data.get("clouds")
            self.wind_speed = data.get("wind_speed")

        @property
        def weather(self):
            try:
                return self.data[0]["main"]
            except:
                return None

    def __init__(self, data):
        self.data = data
        self.lat = data.get("lat")
        self.lon = data.get("lon")

    @property
    def current(self):
        current_data = self.data.get("current")
        if not current_data:
            return None

        return self.Current(current_data)


class CurrentWeatherData:
    def __init__(self, data: dict) -> None:
        self.data = data
        self.lat = data["coord"]["lat"]
        self.lon = data["coord"]["lon"]
        self.weather = data["weather"][0]["main"]
        main_data = data["main"]
        self.temp = main_data["temp"]
        self.feels_like = main_data["feels_like"]
        self.temp_min = main_data["temp_min"]
        self.temp_max = main_data["temp_max"]
        self.pressure = main_data["pressure"]
        self.humidity = main_data["humidity"]
        self.wind_speed = data["wind"]["speed"]

    @property
    def clouds(self):
        try:
            return self.data["clouds"]["all"]
        except:
            return None

    @property
    def rain_1h(self):
        try:
            return self.data["rain"]["1h"]
        except:
            return None


class Area:
    """エリアモデル"""

    def __init__(self, city_name: str):
        self.city_name = city_name
        self.geo_data = None

    def get_area_info(self):
        self.geo_data = geo_coding_api(self.city_name)


class AbstractAPI:
    @classmethod
    def get_weather_data(self, area: Area):
        return NotImplementedError()


class OneCallAPI(AbstractAPI):
    @classmethod
    def get_weather_data(self, area: Area, exclude = None) -> WeatherData:
        lat = area.geo_data.lat
        lon = area.geo_data.lon

        if exclude:
            part = ",".join(exclude)
        else:
            part = ""

        url =f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={settings.API_KEY}"
        response = fetch(url)
        data = response.json()
        return WeatherData(data)


class CurrentWeatherAPI(AbstractAPI):
    @classmethod
    def get_weather_data(self, area: Area):
        lat = area.geo_data.lat
        lon = area.geo_data.lon
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={settings.API_KEY}"
        response = fetch(url)
        data = response.json()
        return CurrentWeatherData(data)
