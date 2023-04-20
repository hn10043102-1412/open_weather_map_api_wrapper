import api


def get_weather_data(city_name: str, use_api: str):
    # エリアインスタンスを作成する
    area = api.Area(city_name=city_name)

    # 天気を調査するための事前情報を獲得する
    area.get_area_info()

    # apiを制御する
    match use_api:
        case "onecall":
            data = api.OneCallAPI.get_weather_data(area=area)
        case "current":
            data = api.CurrentWeatherAPI.get_weather_data(area=area)

    return data


def main():
    current_tokyo_data = get_weather_data(city_name="tokyo", use_api="current")
    print(current_tokyo_data)


if __name__ == "__main__":
    main()
