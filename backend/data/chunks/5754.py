def test_wmts(rio, app):
    """test wmts endpoints."""
    rio.open = mock_rasterio_open

    response = app.get("/cog/WMTSCapabilities.xml?url=https://myurl.com/cog.tif")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/xml"
    assert response.headers["Cache-Control"] == "private, max-age=3600"
    assert (
        "http://testserver/cog/WMTSCapabilities.xml?url=https://myurl.com/cog.tif"
        in response.content.decode()
    )
    assert "<ows:Identifier>cogeo</ows:Identifier>" in response.content.decode()
    assert (
        "http://testserver/cog/tiles/WebMercatorQuad/{TileMatrix}/{TileCol}/{TileRow}@1x.png?url=https"
        in response.content.decode()
    )

    response = app.get(
        "/cog/WMTSCapabilities.xml?url=https://myurl.com/cog.tif&tile_scale=2&tile_format=jpg"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/xml"
    assert (
        "http://testserver/cog/tiles/WebMercatorQuad/{TileMatrix}/{TileCol}/{TileRow}@2x.jpg?url=https"
        in response.content.decode()
    )