def test_get():
    fake_content = b"some fake video bytes"
    response = client.get("/")
    assert response.content == fake_content * 10