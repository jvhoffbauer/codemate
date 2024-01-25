def cookie_examples(
    data: Union[str, None] = Cookie(
        default=None,
        examples=["json_schema_cookie1", "json_schema_cookie2"],
        openapi_examples={
            "Cookie One": {
                "summary": "Cookie One Summary",
                "description": "Cookie One Description",
                "value": "cookie1",
            },
            "Cookie Two": {
                "value": "cookie2",
            },
        },
    ),
):
    return data