    @app.post("/examples/")
    def examples(
        item: Item = Body(
            examples=[
                {"data": "Data in Body examples, example1"},
                {"data": "Data in Body examples, example2"},
            ],
        ),
    ):
        return item