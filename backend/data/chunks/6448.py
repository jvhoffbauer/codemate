@APP.exception_handler(pydantic.error_wrappers.ValidationError)
async def handle_validation_error(
    request: Request, exc: pydantic.error_wrappers.ValidationError
):  # pylint: disable=unused-argument
    """
    Handles validation errors.
    """
    return JSONResponse({"message": exc.errors()}, status_code=422)