    def handler(request: Request, exc: Exception):
        return JSONResponse(content={"detail": str(exc)}, status_code=status_code)