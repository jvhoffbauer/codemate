def test_missing_asset_not_found(httpx, rio, app):
    """test /info endpoint."""
    httpx.get = mock_RequestGet
    rio.open = mock_rasterio_open

    response = app.get(
        "/stac/preview?url=https://myurl.com/item.json&assets=B1111&rescale=0,1000&max_size=64"
    )
    assert response.status_code == 404