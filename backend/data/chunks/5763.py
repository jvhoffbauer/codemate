@patch("rio_tiler.io.rasterio.rasterio")
def test_point(rio, app):
    """test /point endpoint."""
    rio.open = mock_rasterio_open

    response = app.get("/cog/point/-56.228,72.715?url=https://myurl.com/cog.tif")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    body = response.json()
    assert body["coordinates"] == [-56.228, 72.715]