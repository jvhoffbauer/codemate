def test_docs_redirect():
    client = TestClient(app)
    response = client.get("/")
    assert response.history[0].status_code == 302
    assert response.status_code == 200
    assert response.url == "http://testserver/docs"