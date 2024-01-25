async def http_exception_handler(request, exc):
    return ORJSONResponse(
        {
            "detail": exc.detail,
        },
        status_code=exc.status_code,
    )