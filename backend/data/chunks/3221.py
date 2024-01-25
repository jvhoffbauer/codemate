        @app.get("/cookie_example/")
        def cookie_example(
            data: Union[str, None] = Cookie(
                default=None,
                example="cookie1",
            ),
        ):
            return data