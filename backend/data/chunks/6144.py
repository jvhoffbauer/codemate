async def server_error_handler(request: Request, exc: Exception):
    """Internal server exception.Output a json response and throw the exception again."""
    return make_error_response(
        status=HTTP_500_INTERNAL_SERVER_ERROR,
        msg=_("Internal server exception"),
        exc=exc,
    )