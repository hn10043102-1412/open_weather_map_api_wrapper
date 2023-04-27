# 概要
OpenWeatherMapAPIのラッパーライブラリになります。
簡単に書いたため、機能は不完全な部分がほとんどです。

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