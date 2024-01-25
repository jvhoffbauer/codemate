        @app.get("/query_example/")
        def query_example(
            data: Union[str, None] = Query(
                default=None,
                example="query1",
            ),
        ):
            return data