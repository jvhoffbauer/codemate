async def http_exception_handler(request: Request, exc: HTTPException):
    """http exception"""
    headers = getattr(exc, "headers", None)
    if not is_body_allowed_for_status_code(exc.status_code):
        return Response(status_code=exc.status_code, headers=headers)
    content = getattr(exc, "content", {"status": exc.status_code, "msg": exc.detail})
    return JSONResponse(content=content, status_code=exc.status_code, headers=headers)