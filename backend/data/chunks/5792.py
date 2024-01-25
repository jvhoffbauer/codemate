def test_tile(httpx, rio, app):
    """test tile endpoints."""
    httpx.get = mock_RequestGet
    rio.open = mock_rasterio_open

    # Missing assets
    response = app.get("/stac/tiles/9/289/207?url=https://myurl.com/item.json")
    assert response.status_code == 400

    response = app.get(
        "/stac/tiles/9/289/207?url=https://myurl.com/item.json&assets=B01&rescale=0,1000"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    meta = parse_img(response.content)
    assert meta["width"] == 256
    assert meta["height"] == 256

    response = app.get(
        "/stac/tiles/9/289/207?url=https://myurl.com/item.json&expression=B01_b1&rescale=0,1000"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    meta = parse_img(response.content)
    assert meta["width"] == 256
    assert meta["height"] == 256