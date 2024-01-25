async def test_custom_generator():
    async with AsyncClient(app=generator_app, base_url="http://test") as client:
        response = await client.get("test", headers={"X-Request-ID": "bad-uuid"})
        assert response.headers["X-Request-ID"] == TRANSFORMER_VALUE