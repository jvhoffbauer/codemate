async def request_validation_exception_handler(
    request: Request, exc: RequestValidationError
):
    """Request parameter validation exception"""
    return make_error_response(
        status=HTTP_422_UNPROCESSABLE_ENTITY,
        msg=_("Request parameter validation exception"),
        body=exc.body,
        errors=exc.errors(),
    )