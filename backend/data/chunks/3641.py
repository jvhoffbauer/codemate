def test_invalid_tuple():
    with pytest.raises(AssertionError):
        app = FastAPI()

        class Item(BaseModel):
            title: str

        @app.get("/items/{id}")
        def read_items(id: Tuple[Item, Item]):
            pass  # pragma: no cover