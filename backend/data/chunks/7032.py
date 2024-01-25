def test_info_block(app, app_client):
    app.title = "Test App"
    app.version = "1.2.3"
    app.servers = [{"test": "https://test.dev"}]

    resp = app_client.get("/openrpc.json")

    assert resp.json() == {
        "openrpc": "1.2.6",
        "info": {
            "version": app.version,
            "title": app.title,
        },
        "servers": app.servers,
        "methods": [],
        "components": {
            "schemas": {},
            "errors": {},
        },
    }