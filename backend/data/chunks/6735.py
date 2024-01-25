def get_jsonrpc_method() -> Optional[str]:
    return get_jsonrpc_context().raw_request.get("method")