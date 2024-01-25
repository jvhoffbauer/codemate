def test_errors(ep, app, app_client):
    class MyError(jsonrpc.BaseError):
        CODE = 5000
        MESSAGE = "My error"

        class DataModel(BaseModel):
            details: str

    @ep.method(errors=[MyError])
    def my_method__with_errors() -> None:
        return None

    app.bind_entrypoint(ep)

    resp = app_client.get("/openrpc.json")
    schema = resp.json()

    assert len(schema["methods"]) == 1
    assert schema["methods"][0]["errors"] == [
        {"$ref": "#/components/errors/5000"},
    ]
    assert schema["components"]["errors"]["5000"] == {
        "code": 5000,
        "message": "My error",
        "data": {
            "title": "MyError.Data",
            "type": "object",
            "properties": {"details": {"title": "Details", "type": "string"}},
            "required": ["details"],
        },
    }