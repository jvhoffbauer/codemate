def register_exception_handlers(app: FastAPI, **kwargs):
    """global exception catch"""
    app.add_exception_handler(
        RequestValidationError, handler=request_validation_exception_handler
    )
    app.add_exception_handler(HTTPException, handler=http_exception_handler)
    app.add_exception_handler(
        ValidationException, handler=inner_validation_exception_handler
    )
    app.add_exception_handler(
        ValidationError, handler=inner_validation_exception_handler
    )
    app.add_exception_handler(Exception, handler=server_error_handler)