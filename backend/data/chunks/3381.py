def test_invalid_tuple():
    with pytest.raises(AssertionError):
        app = FastAPI()

        class Item(BaseModel):
            title: str

        @app.get("/items/")
        def read_items(q: Tuple[Item, Item] = Query(default=None)):
            pass  # pragma: no cover