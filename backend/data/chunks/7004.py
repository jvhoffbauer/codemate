def test_basic(probe_ep, raw_request):
    body = json_dumps(
        {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "probe",
            "params": {"data": "data-123"},
        }
    )
    response = raw_request(body)
    assert response.cookies["probe-cookie"] == "data-123"
    assert response.cookies["ep_middleware_enter"] == "1"
    assert response.cookies["ep_middleware_exit"] == "2"
    assert response.cookies["method_middleware_enter"] == "3"
    assert response.cookies["method_middleware_exit"] == "4"
    assert response.status_code == 404