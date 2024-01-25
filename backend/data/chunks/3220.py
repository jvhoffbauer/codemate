        def header_example_examples(
            data: Union[str, None] = Header(
                default=None,
                example="header_overridden",
                examples=["header1", "header2"],
            ),
        ):
            return data