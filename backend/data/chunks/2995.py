def get_client():
    app = FastAPI()
    with pytest.warns(DeprecationWarning):

        @app.get("/items/")
        async def read_items(
            q: Annotated[str | None, Query(regex="^fixedquery$")] = None
        ):
            if q:
                return f"Hello {q}"
            else:
                return "Hello World"

    client = TestClient(app)
    return client