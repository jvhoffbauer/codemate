@app.get("/query_examples/")
def query_examples(
    data: Union[str, None] = Query(
        default=None,
        examples=[
            "json_schema_query1",
            "json_schema_query2",
        ],
        openapi_examples={
            "Query One": {
                "summary": "Query One Summary",
                "description": "Query One Description",
                "value": "query1",
            },
            "Query Two": {
                "value": "query2",
            },
        },
    ),
):
    return data