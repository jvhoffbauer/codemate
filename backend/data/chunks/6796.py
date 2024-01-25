@pytest.mark.parametrize("fastapi_jsonrpc_components_fine_names", [True, False])
def test_no_entrypoints__ok(fastapi_jsonrpc_components_fine_names):
    app = jsonrpc.API(
        fastapi_jsonrpc_components_fine_names=fastapi_jsonrpc_components_fine_names
    )
    app_client = TestClient(app)
    resp = app_client.get("/openapi.json")
    resp.raise_for_status()
    assert resp.status_code == 200