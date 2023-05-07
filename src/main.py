import api as open_weather_map_api
import data
from settings import OPEN_WEATHER_MAP_API_KEY


class WeatherDataGetter:
    def __init__(self, city_name: str):
        self.api = open_weather_map_api.OpenWeatherAPI(api_key=OPEN_WEATHER_MAP_API_KEY)
        self.area_geo_data = self.api.get_geo_data(city_name=city_name)
        self.area = data.Area(city_name=city_name, geo_data=self.area_geo_data)

    def get_weather_data(self, use_api: str):
        """
        引数を基に天気情報を取得する関数
        use_api: "onecall" or "current" or "3h5d"
        """
        api_calls = {
            "onecall": self.api.get_weather_data,
            "current": self.api.get_current_weather_data,
            "3h5d": self.api.get_forecast3h5d_weather_data,
        }
        try:
            return api_calls[use_api](area=self.area)
        except KeyError:
            raise ValueError("Invalid value for use_api")


def main():
    tokyo_weather_getter =  WeatherDataGetter(city_name="tokyo")

    # 東京の現在の天気を取得
    current_tokyo_data =tokyo_weather_getter.get_weather_data(use_api="current")
    print(current_tokyo_data)

    # 東京の5日間で３時間ごとの天気を取得
    forecast_3h5d_data = tokyo_weather_getter.get_weather_data(use_api="3h5d")
    print(forecast_3h5d_data)

    forecast_3h5d_list = forecast_3h5d_data.get_three_hourly_weather_list()
    print(forecast_3h5d_list)


if __name__ == "__main__":
    main()
