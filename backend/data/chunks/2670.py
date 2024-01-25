def set_cookie(*, response: Response):
    response.set_cookie("cookie-name", "cookie-value")
    return {}