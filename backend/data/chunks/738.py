async def client() -> AsyncClient:
    async with AsyncClient(app=default_app, base_url="http://test") as client:
        yield client