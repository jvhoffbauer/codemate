def server_error_exception_handler(request, exception):
    return JSONResponse(status_code=500, content={"exception": "server-error"})