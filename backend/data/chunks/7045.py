def test_type_hints(ep, app, app_client):
    Input = List[str]
    Output = Dict[str, List[List[float]]]

    @ep.method()
    def my_method__with_typehints(arg: Input) -> Output:
        return {}

    app.bind_entrypoint(ep)

    resp = app_client.get("/openrpc.json")
    schema = resp.json()

    assert len(schema["methods"]) == 1
    assert schema["methods"][0]["params"] == [
        {
            "name": "arg",
            "schema": {"title": "Arg", "type": "array", "items": {"type": "string"}},
            "required": True,
        }
    ]
    assert schema["methods"][0]["result"] == {
        "name": "my_method__with_typehints_Result",
        "schema": {
            "title": "Result",
            "type": "object",
            "additionalProperties": {
                "type": "array",
                "items": {"type": "array", "items": {"type": "number"}},
            },
        },
    }