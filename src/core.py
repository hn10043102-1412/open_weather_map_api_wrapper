import requests

import error


def fetch(url: str, params = None):
    """HTTPリクエストを行う"""

    response = requests.get(url, params)
    if response.status_code != 200:
        raise error.CheckPriceError(response)

    return response
