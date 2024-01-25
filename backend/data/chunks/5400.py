def add_exception_handlers(
    app: FastAPI, status_codes: Dict[Type[Exception], int]
) -> None:
    """
    Add exception handlers to the FastAPI app.
    """
    for exc, code in status_codes.items():
        app.add_exception_handler(exc, exception_handler_factory(code))