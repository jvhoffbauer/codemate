def exception_handler_factory(status_code: int) -> Callable:
    """
    Create a FastAPI exception handler from a status code.
    """

    def handler(request: Request, exc: Exception):
        return JSONResponse(content={"detail": str(exc)}, status_code=status_code)

    return handler