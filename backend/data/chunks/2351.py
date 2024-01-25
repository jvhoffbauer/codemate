@app.get(
    "/",
    openapi_extra={
        "parameters": [
            {
                "required": False,
                "schema": {"title": "Extra Param 1"},
                "name": "extra_param_1",
                "in": "query",
            },
            {
                "required": True,
                "schema": {"title": "Extra Param 2"},
                "name": "extra_param_2",
                "in": "query",
            },
        ]
    },
)
def route_with_extra_query_parameters(standard_query_param: Optional[int] = 50):
    return {}