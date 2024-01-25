def test_invalid_simple_set():
    with pytest.raises(AssertionError):
        app = FastAPI()

        @app.get("/items/{id}")
        def read_items(id: set):
            pass  # pragma: no cover