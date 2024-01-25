        @app.get("/items/{id}")
        def read_items(id: Tuple[Item, Item]):
            pass  # pragma: no cover