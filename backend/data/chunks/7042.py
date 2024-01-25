def test_errors_merging(ep, app, app_client):
    class FirstError(jsonrpc.BaseError):
        CODE = 5000
        MESSAGE = "My error"

        class DataModel(BaseModel):
            x: str

    class SecondError(jsonrpc.BaseError):
        CODE = 5000
        MESSAGE = "My error"

        class DataModel(BaseModel):
            y: int

    @ep.method(errors=[FirstError, SecondError])
    def my_method__with_mergeable_errors() -> None:
        return None

    app.bind_entrypoint(ep)

    resp = app_client.get("/openrpc.json")
    schema = resp.json()

    assert len(schema["methods"]) == 1
    assert schema["methods"][0]["errors"] == [{"$ref": "#/components/errors/5000"}]
    assert schema["components"]["errors"]["5000"] == {
        "code": 5000,
        "message": "My error",
        "data": {
            "title": "ERROR_5000",
            "anyOf": [
                {"$ref": "#/components/schemas/FirstError.Data"},
                {"$ref": "#/components/schemas/SecondError.Data"},
            ],
        },
    }
    assert schema["components"]["schemas"]["FirstError.Data"] == {
        "title": "FirstError.Data",
        "type": "object",
        "properties": {
            "x": {"type": "string", "title": "X"},
        },
        "required": ["x"],
    }
    assert schema["components"]["schemas"]["SecondError.Data"] == {
        "title": "SecondError.Data",
        "type": "object",
        "properties": {
            "y": {"type": "integer", "title": "Y"},
        },
        "required": ["y"],
    }