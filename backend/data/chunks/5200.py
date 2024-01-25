def unicorn_exception_handler(request: Request, exc: UnicornException):
    return ORJSONResponse(
        status_code=418,
        content={"detail": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )