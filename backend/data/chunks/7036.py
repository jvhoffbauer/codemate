def test_tags(ep, app, app_client):
    @ep.method(tags=["tag1", "tag2"])
    def my_method__with_tags() -> None:
        return None

    app.bind_entrypoint(ep)

    resp = app_client.get("/openrpc.json")
    schema = resp.json()

    assert len(schema["methods"]) == 1
    assert schema["methods"][0]["tags"] == [
        {"name": "tag1"},
        {"name": "tag2"},
    ]