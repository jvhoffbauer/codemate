async def test_non_uuid_header(client, caplog, value, app):
    """
    We expect the middleware to ignore our request ID and log a warning
    when the request ID we pass doesn't correspond to the uuid4 format.
    """

    @app.get("/test", status_code=200)
    async def test_view() -> dict:
        logger.debug("Test view")
        return {"test": "test"}

    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("test", headers={"X-Request-ID": value})
        new_value = response.headers["X-Request-ID"]
        assert new_value != value
        assert caplog.messages[0] == FAILED_VALIDATION_MESSAGE.replace("%s", new_value)