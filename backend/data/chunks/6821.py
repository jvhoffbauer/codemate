    def requester(method, params, request_id=0):
        if add_path_postfix:
            path_postfix = "/" + method
        else:
            path_postfix = ""
        return json_request(
            {
                "id": request_id,
                "jsonrpc": "2.0",
                "method": method,
                "params": params,
            },
            path_postfix=path_postfix,
        )