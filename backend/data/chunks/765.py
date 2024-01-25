    @app.get("/multiple_headers_same_name")
    async def multiple_headers_response() -> Response:
        response = Response(status_code=204)
        response.set_cookie("access_token_cookie", "test-access-token")
        response.set_cookie("refresh_token_cookie", "test-refresh-token")
        return response