def test_redoc_html(client: TestClient):
    response = client.get("/redoc")
    assert response.status_code == 200, response.text
    assert "https://unpkg.com/redoc@next/bundles/redoc.standalone.js" in response.text