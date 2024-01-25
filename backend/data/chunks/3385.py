        @app.get("/items/")
        def read_items(q: Dict[str, Item] = Query(default=None)):
            pass  # pragma: no cover