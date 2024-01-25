        @app.get("/path_example/{item_id}")
        def path_example(
            item_id: str = Path(
                example="item_1",
            ),
        ):
            return item_id