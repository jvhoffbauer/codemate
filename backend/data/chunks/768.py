async def test_custom_transformer():
    cid = uuid4().hex
    async with AsyncClient(app=transformer_app, base_url="http://test") as client:
        response = await client.get("test", headers={"X-Request-ID": cid})
        assert response.headers["X-Request-ID"] == cid * 2