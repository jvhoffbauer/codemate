def test_bounds(rio, app):
    """test /bounds endpoint."""
    rio.open = mock_rasterio_open

    response = app.get("/cog/bounds?url=https://myurl.com/cog.tif")
    assert response.status_code == 200
    body = response.json()
    assert len(body["bounds"]) == 4
    assert response.headers["Cache-Control"] == "private, max-age=3600"