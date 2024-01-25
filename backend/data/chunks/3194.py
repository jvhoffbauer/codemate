def create_app():
    app = FastAPI()

    class Item(BaseModel):
        data: str

        if PYDANTIC_V2:
            model_config = ConfigDict(
                json_schema_extra={"example": {"data": "Data in schema_extra"}}
            )
        else:

            class Config:
                schema_extra = {"example": {"data": "Data in schema_extra"}}

    @app.post("/schema_extra/")
    def schema_extra(item: Item):
        return item

    with pytest.warns(DeprecationWarning):

        @app.post("/example/")
        def example(item: Item = Body(example={"data": "Data in Body example"})):
            return item

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

    with pytest.warns(DeprecationWarning):

        @app.post("/example_examples/")
        def example_examples(
            item: Item = Body(
                example={"data": "Overridden example"},
                examples=[
                    {"data": "examples example_examples 1"},
                    {"data": "examples example_examples 2"},
                ],
            ),
        ):
            return item

    # TODO: enable these tests once/if Form(embed=False) is supported
    # TODO: In that case, define if File() should support example/examples too
    # @app.post("/form_example")
    # def form_example(firstname: str = Form(example="John")):
    #     return firstname

    # @app.post("/form_examples")
    # def form_examples(
    #     lastname: str = Form(
    #         ...,
    #         examples={
    #             "example1": {"summary": "last name summary", "value": "Doe"},
    #             "example2": {"value": "Doesn't"},
    #         },
    #     ),
    # ):
    #     return lastname

    # @app.post("/form_example_examples")
    # def form_example_examples(
    #     lastname: str = Form(
    #         ...,
    #         example="Doe overridden",
    #         examples={
    #             "example1": {"summary": "last name summary", "value": "Doe"},
    #             "example2": {"value": "Doesn't"},
    #         },
    #     ),
    # ):
    #     return lastname

    with pytest.warns(DeprecationWarning):

        @app.get("/path_example/{item_id}")
        def path_example(
            item_id: str = Path(
                example="item_1",
            ),
        ):
            return item_id

    @app.get("/path_examples/{item_id}")
    def path_examples(
        item_id: str = Path(
            examples=["item_1", "item_2"],
        ),
    ):
        return item_id

    with pytest.warns(DeprecationWarning):

        @app.get("/path_example_examples/{item_id}")
        def path_example_examples(
            item_id: str = Path(
                example="item_overridden",
                examples=["item_1", "item_2"],
            ),
        ):
            return item_id

    with pytest.warns(DeprecationWarning):

        @app.get("/query_example/")
        def query_example(
            data: Union[str, None] = Query(
                default=None,
                example="query1",
            ),
        ):
            return data

    @app.get("/query_examples/")
    def query_examples(
        data: Union[str, None] = Query(
            default=None,
            examples=["query1", "query2"],
        ),
    ):
        return data

    with pytest.warns(DeprecationWarning):

        @app.get("/query_example_examples/")
        def query_example_examples(
            data: Union[str, None] = Query(
                default=None,
                example="query_overridden",
                examples=["query1", "query2"],
            ),
        ):
            return data

    with pytest.warns(DeprecationWarning):

        @app.get("/header_example/")
        def header_example(
            data: Union[str, None] = Header(
                default=None,
                example="header1",
            ),
        ):
            return data

    @app.get("/header_examples/")
    def header_examples(
        data: Union[str, None] = Header(
            default=None,
            examples=[
                "header1",
                "header2",
            ],
        ),
    ):
        return data

    with pytest.warns(DeprecationWarning):

        @app.get("/header_example_examples/")
        def header_example_examples(
            data: Union[str, None] = Header(
                default=None,
                example="header_overridden",
                examples=["header1", "header2"],
            ),
        ):
            return data

    with pytest.warns(DeprecationWarning):

        @app.get("/cookie_example/")
        def cookie_example(
            data: Union[str, None] = Cookie(
                default=None,
                example="cookie1",
            ),
        ):
            return data

    @app.get("/cookie_examples/")
    def cookie_examples(
        data: Union[str, None] = Cookie(
            default=None,
            examples=["cookie1", "cookie2"],
        ),
    ):
        return data

    with pytest.warns(DeprecationWarning):

        @app.get("/cookie_example_examples/")
        def cookie_example_examples(
            data: Union[str, None] = Cookie(
                default=None,
                example="cookie_overridden",
                examples=["cookie1", "cookie2"],
            ),
        ):
            return data

    return app