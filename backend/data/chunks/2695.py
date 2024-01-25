def test_value_extracting_by_ws():
    with client.websocket_connect("/ws") as websocket:
        assert websocket.receive_json() == 42