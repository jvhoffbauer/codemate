def make_error_response(status: int, msg="", *, exc: Exception = None, **extra):
    """Construct an error response"""
    result = BaseApiOut(status=status, msg=msg, **extra)
    return JSONResponseWithException(content=result.dict(), exc=exc)