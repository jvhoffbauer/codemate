@patch("rio_tiler.io.rasterio.rasterio")
def test_part(rio, app):
    """test /crop endpoint."""
    rio.open = mock_rasterio_open

    response = app.get(
        "/cog/crop/-56.228,72.715,-54.547,73.188.png?url=https://myurl.com/cog.tif&rescale=0,1000&max_size=256"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    meta = parse_img(response.content)
    assert meta["count"] == 2
    assert meta["width"] == 256
    assert meta["height"] == 73
    assert meta["driver"] == "PNG"

    response = app.get(
        "/cog/crop/-56.228,72.715,-54.547,73.188.jpg?url=https://myurl.com/cog.tif&rescale=0,1000&max_size=256&return_mask=false"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpg"
    meta = parse_img(response.content)
    assert meta["count"] == 1
    assert meta["width"] == 256
    assert meta["height"] == 73
    assert meta["driver"] == "JPEG"

    response = app.get(
        "/cog/crop/-56.228,72.715,-54.547,73.188/128x128.png?url=https://myurl.com/cog.tif&rescale=0,1000&max_size=256"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    meta = parse_img(response.content)
    assert meta["width"] == 128
    assert meta["height"] == 128
    assert meta["driver"] == "PNG"

    response = app.get(
        "/cog/crop/-56.228,72.715,-54.547,73.188.png?url=https://myurl.com/cog.tif&rescale=0,1000&max_size=256&width=512&height=512"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    meta = parse_img(response.content)
    assert meta["width"] == 512
    assert meta["height"] == 512
    assert meta["driver"] == "PNG"

    response = app.get(
        "/cog/crop/-56.228,72.715,-54.547,73.188.npy?url=https://myurl.com/cog.tif&rescale=0,1000&max_size=256"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/x-binary"
    data = numpy.load(BytesIO(response.content))
    assert data.shape == (2, 73, 256)