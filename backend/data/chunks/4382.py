def test_get():
    response = client.get("/")
    assert response.content == b'{\n  "message": "Hello World"\n}'