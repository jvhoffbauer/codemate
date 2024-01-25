def path_examples(
    item_id: str = Path(
        examples=[
            "json_schema_item_1",
            "json_schema_item_2",
        ],
        openapi_examples={
            "Path One": {
                "summary": "Path One Summary",
                "description": "Path One Description",
                "value": "item_1",
            },
            "Path Two": {
                "value": "item_2",
            },
        },
    ),
):
    return item_id