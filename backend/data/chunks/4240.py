def test_get():
    response = client.get("/unicorns/shinny")
    assert response.status_code == 200, response.text
    assert response.json() == {"unicorn_name": "shinny"}