def probe(ep):
    @ep.method()
    def probe(
        jsonrpc_request_id: int = Depends(get_jsonrpc_request_id),
    ) -> int:
        return jsonrpc_request_id

    return ep