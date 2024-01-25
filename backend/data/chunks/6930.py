    @ep.method()
    def probe(
        jsonrpc_method: str = Depends(get_jsonrpc_method),
    ) -> str:
        return jsonrpc_method