    @app.get("/cookie_examples/")
    def cookie_examples(
        data: Union[str, None] = Cookie(
            default=None,
            examples=["cookie1", "cookie2"],
        ),
    ):
        return data