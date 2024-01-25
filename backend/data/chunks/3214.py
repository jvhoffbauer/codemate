        def query_example_examples(
            data: Union[str, None] = Query(
                default=None,
                example="query_overridden",
                examples=["query1", "query2"],
            ),
        ):
            return data