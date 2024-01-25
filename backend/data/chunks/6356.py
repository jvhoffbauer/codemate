@pytest.fixture
async def async_client(
    app: FastAPI, prepare_database: Any
) -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://testserver") as c:
        yield c