# 概要
このマークダウンは、OpenWeatherMapAPIのPythonライブラリに関するもので、APIをより簡単に使用できるようにしています。
Pythonのrequestsとpython-dotenvの2つのモジュールをインストールする必要があります。
また、動作検証のために、OpenWeatherMapのサイトでAPIキーを発行し、`.env`ファイルを作成してAPIキーを定義する必要があります。
API referenceには、現在の天気、5日間の予報、One Call API、ジオコーディングAPIが含まれています。
ただし、このライブラリは機能が不完全な部分があるため、注意が必要です。

# インストール
```shell:
$ pip3 install requests python-dotenv
```

# 動作検証
1. OpenWeatherMapのサイトにてAPIキーを発行してください。
2. フォルダ直下に`.env`ファイルを作成してください
3. `OPEN_WEATHER_API_KEY`にAPIキーを定義してください。
4. `main.py`を実行してください。

# API reference
- https://openweathermap.org/current
- https://openweathermap.org/forecast5
- https://openweathermap.org/api/one-call-3
- https://openweathermap.org/api/geocoding-api