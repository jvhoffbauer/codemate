def body():
    return json_dumps(
        {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "probe",
            "params": {},
        }
    )