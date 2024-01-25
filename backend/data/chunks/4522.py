def test_path_operation():
    response = client.get("/headers/")
    assert response.status_code == 200, response.text
    assert response.json() == {"message": "Hello World"}
    assert response.headers["X-Cat-Dog"] == "alone in the world"
    assert response.headers["Content-Language"] == "en-US"