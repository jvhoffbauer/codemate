async def test_update_request_header(app):
    """
    We expect the middleware to update the request header with the request ID
    value.
    """

    @app.get("/test", status_code=200)
    async def test_view(request: Request) -> dict:
        logger.debug("Test view")
        return {"correlation_id": request.headers.get("X-Request-ID")}

    async with AsyncClient(app=app, base_url="http://test") as client:
        # Check for newly generated request ID in the request header if none
        # was initially provided.
        response = await client.get("test")
        assert is_valid_uuid4(response.json()["correlation_id"])

        # Check for newly generated request ID in the request header if it
        # initially contains an invalid value.
        response = await client.get("test", headers={"X-Request-ID": "invalid"})
        assert is_valid_uuid4(response.json()["correlation_id"])

        # Check for our request ID value in the request header.
        correlation_id = uuid4().hex
        response = await client.get("test", headers={"X-Request-ID": correlation_id})
        assert response.json()["correlation_id"] == correlation_id