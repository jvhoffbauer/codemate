        @app.get("/path_example_examples/{item_id}")
        def path_example_examples(
            item_id: str = Path(
                example="item_overridden",
                examples=["item_1", "item_2"],
            ),
        ):
            return item_id