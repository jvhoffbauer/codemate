        @app.get("/cookie_example_examples/")
        def cookie_example_examples(
            data: Union[str, None] = Cookie(
                default=None,
                example="cookie_overridden",
                examples=["cookie1", "cookie2"],
            ),
        ):
            return data