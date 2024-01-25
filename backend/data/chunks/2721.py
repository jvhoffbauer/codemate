def test_trace():
    response = client.request("trace", "/items/foo")
    assert response.status_code == 200, response.text
    assert response.headers["content-type"] == "message/http"