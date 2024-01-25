def test_invalid_simple_tuple():
    with pytest.raises(AssertionError):
        app = FastAPI()

        @app.get("/items/{id}")
        def read_items(id: tuple):
            pass  # pragma: no cover