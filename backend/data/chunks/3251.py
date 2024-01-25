def http_exception_handler(request, exception):
    return JSONResponse({"exception": "http-exception"})