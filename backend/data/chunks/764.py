async def test_multiple_headers_same_name(caplog, app):
    """
    The middleware should not change the headers that were set in the response and return all of them as it is.
    """

    @app.get("/multiple_headers_same_name")
    async def multiple_headers_response() -> Response:
        response = Response(status_code=204)
        response.set_cookie("access_token_cookie", "test-access-token")
        response.set_cookie("refresh_token_cookie", "test-refresh-token")
        return response

    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("multiple_headers_same_name")
        assert response.headers["set-cookie"].find("access_token_cookie") != -1
        assert response.headers["set-cookie"].find("refresh_token_cookie") != -1