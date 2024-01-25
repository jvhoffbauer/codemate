def test_invalid_simple_dict():
    with pytest.raises(AssertionError):
        app = FastAPI()

        @app.get("/items/{id}")
        def read_items(id: dict):
            pass  # pragma: no cover