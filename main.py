import api
import data


def get_weather_data(city_name: str, use_api: str):
    """
    引数を基に天気情報を取得する関数
    use_api: "onecall" or "current" or "3h5d"
    """

    # 天気を調査するための事前情報を獲得する
    area_geo_data = api.GeoCogingAPI.get_geo_data(city_name=city_name)

    # エリアインスタンスを作成する
    area = data.Area(city_name=city_name, geo_data=area_geo_data)

    # apiを制御する
    match use_api:
        case "onecall":
            result = api.OneCallAPI.get_weather_data(area=area)
        case "current":
            result = api.CurrentWeatherAPI.get_weather_data(area=area)
        case "3h5d":
            result = api.Forecast3h5dWeatherAPI.get_weather_data(area=area)

    return result


def main():
    # 東京の現在の天気を取得
    # current_tokyo_data = get_weather_data(city_name="tokyo", use_api="current")
    # print(current_tokyo_data)

    # 東京の5日間で３時間ごとの天気を取得
    forecast_3h5d_data = get_weather_data(city_name="tokyo", use_api="3h5d")
    print(forecast_3h5d_data)
    forecast_3h5d_list = forecast_3h5d_data.get_three_hourly_weather_list()
    print(forecast_3h5d_list)


if __name__ == "__main__":
    main()
