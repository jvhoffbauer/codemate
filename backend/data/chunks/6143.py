async def inner_validation_exception_handler(
    request: Request, exc: typing.Union[ValidationException, ValidationError]
):
    """Internal data validation exception.Output a json response and throw the exception again."""
    return make_error_response(
        status=HTTP_417_EXPECTATION_FAILED,
        msg=_("Internal data validation exception"),
        errors=exc.errors(),
        exc=exc,
    )