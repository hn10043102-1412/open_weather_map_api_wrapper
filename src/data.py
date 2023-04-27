class GeoData:
    """地理情報データモデル"""

    def __init__(self, data: dict) -> None:
        self.data = data
        self.name = data.get("name")
        self.lat = data.get("lat")
        self.lon = data.get("lon")


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
    """現在の天気モデル"""

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


class Forecast3h5dWeatherData:
    """予報天気モデル"""

    class ThreeHourly:
        """3時間ごとの天気モデル"""
        def __init__(self, data: dict) -> None:
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

    def __init__(self, data: dict) -> None:
        self.data = data
        self.lat = data["city"]["coord"]["lat"]
        self.lon = data["city"]["coord"]["lon"]

    def get_three_hourly_weather_list(self):
        data = self.data.get("list")
        return [self.ThreeHourly(weather) for weather in data]


class Area:
    """エリアモデル"""

    def __init__(self, city_name: str, geo_data: GeoData):
        self.city_name = city_name
        self.geo_data = geo_data
