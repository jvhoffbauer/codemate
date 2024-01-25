def test_invalid_simple_dict():
    with pytest.raises(AssertionError):
        app = FastAPI()

        class Item(BaseModel):
            title: str

        @app.get("/items/")
        def read_items(q: Optional[dict] = Query(default=None)):
            pass  # pragma: no cover