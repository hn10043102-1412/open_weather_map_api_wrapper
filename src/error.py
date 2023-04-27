class HTTPRequestError(Exception):
    pass


class CheckPriceError(HTTPRequestError):
    """有料のAPIを利用した、もしくは無料枠を超えたエラー"""
    pass
