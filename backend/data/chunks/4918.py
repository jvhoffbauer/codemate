@needs_py310
def test_post_uploadfile_no_body(client: TestClient):
    response = client.post("/uploadfile/")
    assert response.status_code == 200, response.text
    assert response.json() == {"message": "No upload file sent"}