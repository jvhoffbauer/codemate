def test_get_exception():
    response = client.get("/unicorns/yolo")
    assert response.status_code == 418, response.text
    assert response.json() == {
        "message": "Oops! yolo did something. There goes a rainbow..."
    }