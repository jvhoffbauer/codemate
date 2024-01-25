def test_post_form_no_body(client: TestClient):
    response = client.post("/files/")
    assert response.status_code == 200, response.text
    assert response.json() == {"message": "No file sent"}