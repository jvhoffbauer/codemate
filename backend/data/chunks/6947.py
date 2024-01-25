@pytest.fixture
def ep(ep_path):
    class CustomJsonRpcRequest(JsonRpcRequest):
        extra_value: str

    ep = Entrypoint(ep_path, request_class=CustomJsonRpcRequest)

    @ep.method()
    def probe(
        jsonrpc_method: str = Depends(get_jsonrpc_method),
    ) -> str:
        return jsonrpc_method

    return ep