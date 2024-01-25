def header_examples(
    data: Union[str, None] = Header(
        default=None,
        examples=[
            "json_schema_header1",
            "json_schema_header2",
        ],
        openapi_examples={
            "Header One": {
                "summary": "Header One Summary",
                "description": "Header One Description",
                "value": "header1",
            },
            "Header Two": {
                "value": "header2",
            },
        },
    ),
):
    return data