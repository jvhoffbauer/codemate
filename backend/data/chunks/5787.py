def test_bounds(httpx, app):
    """test /bounds endpoint."""
    httpx.get = mock_RequestGet

    response = app.get("/stac/bounds?url=https://myurl.com/item.json")
    assert response.status_code == 200
    body = response.json()
    assert len(body["bounds"]) == 4