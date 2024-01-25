def test_wmts(app):
    """test GET /mosaicjson/WMTSCapabilities.xml endpoint"""
    with patch.object(FileBackend, "_read", mosaic_read_factory(MOSAICJSON_FILE)):
        response = app.get(
            "/mosaicjson/WMTSCapabilities.xml", params={"url": MOSAICJSON_FILE}
        )
        assert response.status_code == 200
        assert response.headers["content-type"] == "application/xml"
        assert (
            "http://testserver/mosaicjson/tiles/WebMercatorQuad/{TileMatrix}/{TileCol}/{TileRow}@1x.png?url="
            in response.content.decode()
        )

        response = app.get(
            "/mosaicjson/WMTSCapabilities.xml",
            params={"url": MOSAICJSON_FILE, "tile_scale": 2},
        )
        assert response.status_code == 200
        assert response.headers["content-type"] == "application/xml"
        assert (
            "http://testserver/mosaicjson/tiles/WebMercatorQuad/{TileMatrix}/{TileCol}/{TileRow}@2x.png?url="
            in response.content.decode()
        )