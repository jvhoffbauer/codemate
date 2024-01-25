@patch("rio_tiler.io.rasterio.rasterio")
def test_preview(rio, app):
    """test /preview endpoint."""
    rio.open = mock_rasterio_open

    response = app.get(
        "/cog/preview?url=https://myurl.com/cog.tif&rescale=0,1000&max_size=256"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"
    meta = parse_img(response.content)
    assert meta["width"] == 256
    assert meta["height"] == 256
    assert meta["driver"] == "JPEG"

    response = app.get(
        "/cog/preview.png?url=https://myurl.com/cog.tif&rescale=0,1000&max_size=256"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    meta = parse_img(response.content)
    assert meta["count"] == 2
    assert meta["width"] == 256
    assert meta["height"] == 256
    assert meta["driver"] == "PNG"

    response = app.get(
        "/cog/preview.png?url=https://myurl.com/cog.tif&rescale=0,1000&max_size=256&return_mask=false"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    meta = parse_img(response.content)
    assert meta["count"] == 1
    assert meta["width"] == 256
    assert meta["height"] == 256
    assert meta["driver"] == "PNG"

    response = app.get(
        "/cog/preview.png?url=https://myurl.com/cog.tif&rescale=0,1000&max_size=128&width=512&height=512"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    meta = parse_img(response.content)
    assert meta["width"] == 512
    assert meta["height"] == 512
    assert meta["driver"] == "PNG"

    response = app.get(
        "/cog/preview.npy?url=https://myurl.com/cog.tif&rescale=0,1000&max_size=1024"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/x-binary"
    data = numpy.load(BytesIO(response.content))
    assert data.shape == (2, 1024, 1021)