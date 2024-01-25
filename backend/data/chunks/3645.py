        @app.get("/items/{id}")
        def read_items(id: Dict[str, Item]):
            pass  # pragma: no cover