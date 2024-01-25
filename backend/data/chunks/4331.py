def test_main():
    response = client.get("/app")
    assert response.status_code == 200, response.text
    assert response.json() == {"message": "Hello World from main app"}