def test_invalid_simple_list():
    with pytest.raises(AssertionError):
        app = FastAPI()

        @app.get("/items/{id}")
        def read_items(id: list):
            pass  # pragma: no cover