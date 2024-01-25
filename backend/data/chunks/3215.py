        @app.get("/header_example/")
        def header_example(
            data: Union[str, None] = Header(
                default=None,
                example="header1",
            ),
        ):
            return data