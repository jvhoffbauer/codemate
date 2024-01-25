    def query_examples(
        data: Union[str, None] = Query(
            default=None,
            examples=["query1", "query2"],
        ),
    ):
        return data