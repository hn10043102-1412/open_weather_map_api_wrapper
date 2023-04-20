import api
import data


def get_weather_data(city_name: str, use_api: str):
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

    return result


def main():
    current_tokyo_data = get_weather_data(city_name="tokyo", use_api="current")
    print(current_tokyo_data)


if __name__ == "__main__":
    main()
