def test_dict_error(echo, json_request):
    resp = json_request("qwe")
    assert resp == {
        "error": {
            "code": -32600,
            "message": "Invalid Request",
            "data": {
                "errors": [
                    {
                        "ctx": {"class_name": "_Request"},
                        "input": "qwe",
                        "loc": [],
                        "msg": "Input should be a valid dictionary or instance of _Request",
                        "type": "model_type",
                    }
                ]
            },
        },
        "id": None,
        "jsonrpc": "2.0",
    }
    assert echo.history == []