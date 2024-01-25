def test_tile(rio, app):
    """test tile endpoints."""
    rio.open = mock_rasterio_open

    # full tile
    response = app.get(
        "/cog/tiles/8/87/48?url=https://myurl.com/cog.tif&rescale=0,1000"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"
    assert response.headers["Cache-Control"] == "private, max-age=3600"
    meta = parse_img(response.content)
    assert meta["width"] == 256
    assert meta["height"] == 256

    response = app.get(
        "/cog/tiles/8/87/48@2x?url=https://myurl.com/cog.tif&rescale=0,1000&color_formula=Gamma R 3"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"
    meta = parse_img(response.content)
    assert meta["width"] == 512
    assert meta["height"] == 512

    response = app.get(
        "/cog/tiles/8/87/48.jpg?url=https://myurl.com/cog.tif&rescale=0,1000"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpg"

    response = app.get(
        "/cog/tiles/8/87/48.jpeg?url=https://myurl.com/cog.tif&rescale=0,1000"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"

    response = app.get(
        "/cog/tiles/8/87/48@2x.jpg?url=https://myurl.com/cog.tif&rescale=0,1000"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpg"

    response = app.get(
        "/cog/tiles/8/87/48@2x.tif?url=https://myurl.com/cog.tif&nodata=0&bidx=1"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/tiff; application=geotiff"
    meta = parse_img(response.content)
    assert meta["dtype"] == "uint16"
    assert meta["count"] == 2
    assert meta["width"] == 512
    assert meta["height"] == 512

    response = app.get("/cog/tiles/8/87/48.npy?url=https://myurl.com/cog.tif&nodata=0")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/x-binary"
    data = numpy.load(BytesIO(response.content))
    assert data.shape == (2, 256, 256)

    response = app.get(
        "/cog/tiles/8/87/48.npy?url=https://myurl.com/cog.tif&nodata=0&return_mask=false"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/x-binary"
    data = numpy.load(BytesIO(response.content))
    assert data.shape == (1, 256, 256)

    # Test brotli compression
    headers = {"Accept-Encoding": "br"}
    response = app.get(
        "/cog/tiles/8/87/48.npy?url=https://myurl.com/cog.tif&nodata=0&return_mask=false",
        headers=headers,
    )
    assert response.status_code == 200
    assert response.headers["content-encoding"] == "br"

    # Exclude png from compression middleware
    headers = {"Accept-Encoding": "br"}
    response = app.get(
        "/cog/tiles/8/87/48.png?url=https://myurl.com/cog.tif&nodata=0&return_mask=false",
        headers=headers,
    )
    assert response.status_code == 200
    assert "content-encoding" not in response.headers

    # Test gzip fallback
    headers = {"Accept-Encoding": "gzip"}
    response = app.get(
        "/cog/tiles/8/87/48.npy?url=https://myurl.com/cog.tif&nodata=0&return_mask=false",
        headers=headers,
    )
    assert response.status_code == 200
    assert response.headers["content-encoding"] == "gzip"

    # partial
    response = app.get(
        "/cog/tiles/8/84/47?url=https://myurl.com/cog.tif&rescale=0,1000"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"

    response = app.get(
        "/cog/tiles/8/84/47?url=https://myurl.com/cog.tif&nodata=0&rescale=0,1000&colormap_name=viridis"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"

    cmap = urlencode(
        {
            "colormap": json.dumps(
                {
                    "1": [58, 102, 24, 255],
                    "2": [100, 177, 41],
                    "3": "#b1b129",
                    "4": "#ddcb9aFF",
                }
            )
        }
    )
    response = app.get(
        f"/cog/tiles/8/53/50.png?url=https://myurl.com/above_cog.tif&bidx=1&{cmap}"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"

    cmap = urlencode({"colormap": json.dumps({"1": [58, 102]})})
    response = app.get(
        f"/cog/tiles/8/53/50.png?url=https://myurl.com/above_cog.tif&bidx=1&{cmap}"
    )
    assert response.status_code == 400

    cmap = urlencode({"colormap": {"1": "#ddcb9aFF"}})
    response = app.get(
        f"/cog/tiles/8/53/50.png?url=https://myurl.com/above_cog.tif&bidx=1&{cmap}"
    )
    assert response.status_code == 400

    response = app.get(
        "/cog/tiles/8/53/50.png?url=https://myurl.com/above_cog.tif&bidx=1&resampling=somethingwrong"
    )
    assert response.status_code == 422

    response = app.get(
        "/cog/tiles/8/87/48@2x.tif?url=https://myurl.com/cog.tif&nodata=0&bidx=1&return_mask=false"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/tiff; application=geotiff"
    meta = parse_img(response.content)
    assert meta["dtype"] == "uint16"
    assert meta["count"] == 1
    assert meta["width"] == 512
    assert meta["height"] == 512