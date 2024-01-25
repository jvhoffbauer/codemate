@patch("rio_tiler.io.rasterio.rasterio")
@patch("rio_tiler.io.stac.httpx")
def test_preview(httpx, rio, app):
    """test preview endpoints."""
    httpx.get = mock_RequestGet
    rio.open = mock_rasterio_open

    # Missing Assets or Expression
    response = app.get("/stac/preview?url=https://myurl.com/item.json")
    assert response.status_code == 400

    response = app.get(
        "/stac/preview?url=https://myurl.com/item.json&assets=B01&rescale=0,1000&max_size=64"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    meta = parse_img(response.content)
    assert meta["width"] == 64
    assert meta["height"] == 64

    response = app.get(
        "/stac/preview?url=https://myurl.com/item.json&assets=B01&rescale=0,1000&max_size=64&width=128&height=128"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    meta = parse_img(response.content)
    assert meta["width"] == 128
    assert meta["height"] == 128

    response = app.get(
        "/stac/preview?url=https://myurl.com/item.json&expression=B01_b1&rescale=0,1000&max_size=64"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    meta = parse_img(response.content)
    assert meta["width"] == 64
    assert meta["height"] == 64