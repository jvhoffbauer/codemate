@pytest.mark.parametrize(
    "app", [default_app, no_validator_or_transformer_app, generator_app]
)
async def test_returned_response_headers(app):
    """
    We expect our request id header to be returned back to us.
    """

    @app.get("/test", status_code=200)
    async def test_view() -> dict:
        logger.debug("Test view")
        return {"test": "test"}

    async with AsyncClient(app=app, base_url="http://test") as client:
        # Check we get the right headers back
        correlation_id = uuid4().hex
        response = await client.get("test", headers={"X-Request-ID": correlation_id})
        assert response.headers["X-Request-ID"] == correlation_id

        # And do it one more time, jic
        second_correlation_id = uuid4().hex
        second_response = await client.get(
            "test", headers={"X-Request-ID": second_correlation_id}
        )
        assert second_response.headers["X-Request-ID"] == second_correlation_id

        # Then try without specifying a request id
        third_response = await client.get("test")
        assert third_response.headers["X-Request-ID"] not in [
            correlation_id,
            second_correlation_id,
        ]