def request_validation_exception_handler(request, exception):
    return JSONResponse({"exception": "request-validation"})