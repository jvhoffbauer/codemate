async def test_no_validator():
    async with AsyncClient(
        app=no_validator_or_transformer_app, base_url="http://test"
    ) as client:
        response = await client.get("test", headers={"X-Request-ID": "bad-uuid"})
        assert response.headers["X-Request-ID"] == "bad-uuid"