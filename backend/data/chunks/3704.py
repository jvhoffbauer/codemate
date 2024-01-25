def examples(
    item: Item = Body(
        examples=[
            {"data": "Data in Body examples, example1"},
        ],
        openapi_examples={
            "Example One": {
                "summary": "Example One Summary",
                "description": "Example One Description",
                "value": {"data": "Data in Body examples, example1"},
            },
            "Example Two": {
                "value": {"data": "Data in Body examples, example2"},
            },
        },
    ),
):
    return item