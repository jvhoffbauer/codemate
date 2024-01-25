def test_invalid_dict():
    with pytest.raises(AssertionError):
        app = FastAPI()

        class Item(BaseModel):
            title: str

        @app.get("/items/")
        def read_items(q: Dict[str, Item] = Query(default=None)):
            pass  # pragma: no cover