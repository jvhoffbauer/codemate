def test_websocket():
    with client.websocket_connect("/items/portal-gun") as websocket:
        data = websocket.receive_json()
        assert data == {"item_id": "portal-gun", "path": "/items/{item_id}"}