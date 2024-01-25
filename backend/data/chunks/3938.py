@needs_py310
def test_get_redirect(client: TestClient):
    response = client.get("/portal", params={"teleport": True}, follow_redirects=False)
    assert response.status_code == 307, response.text
    assert response.headers["location"] == "https://www.youtube.com/watch?v=dQw4w9WgXcQ"