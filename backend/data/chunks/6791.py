def test_entrypoint_tags__append_to_method_tags(app, app_client):
    tagged_api = jsonrpc.Entrypoint("/tagged-entrypoint", tags=["jsonrpc"])

    @tagged_api.method()
    async def not_tagged_method(data: dict) -> dict:
        pass

    @tagged_api.method(tags=["method-tag"])
    async def tagged_method(data: dict) -> dict:
        pass

    app.bind_entrypoint(tagged_api)

    resp = app_client.get("/openapi.json")
    resp_json = resp.json()

    assert resp_json["paths"]["/tagged-entrypoint"]["post"]["tags"] == ["jsonrpc"]
    assert resp_json["paths"]["/tagged-entrypoint/not_tagged_method"]["post"][
        "tags"
    ] == ["jsonrpc"]
    assert resp_json["paths"]["/tagged-entrypoint/tagged_method"]["post"]["tags"] == [
        "jsonrpc",
        "method-tag",
    ]