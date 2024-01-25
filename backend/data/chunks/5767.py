def test_tile_outside_bounds_error(rio, app):
    """raise 404 when tile is not found."""
    rio.open = mock_rasterio_open

    response = app.get("/cog/tiles/15/0/0?url=https://myurl.com/cog.tif&rescale=0,1000")
    assert response.status_code == 404
    assert response.headers["Cache-Control"] == "private, max-age=3600"