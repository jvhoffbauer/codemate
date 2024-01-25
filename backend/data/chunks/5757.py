@patch("rio_tiler.io.rasterio.rasterio")
def test_tilejson(rio, app):
    """test /tilejson endpoint."""
    rio.open = mock_rasterio_open

    response = app.get("/cog/tilejson.json?url=https://myurl.com/cog.tif")
    assert response.status_code == 200
    body = response.json()
    assert body["tilejson"] == "2.2.0"
    assert body["version"] == "1.0.0"
    assert body["scheme"] == "xyz"
    assert len(body["tiles"]) == 1
    assert body["tiles"][0].startswith(
        "http://testserver/cog/tiles/WebMercatorQuad/{z}/{x}/{y}@1x?url=https"
    )
    assert body["minzoom"] == 5
    assert body["maxzoom"] == 9
    assert body["bounds"]
    assert body["center"]

    response = app.get(
        "/cog/tilejson.json?url=https://myurl.com/cog.tif&tile_format=png&tile_scale=2"
    )
    assert response.status_code == 200
    body = response.json()
    assert body["tiles"][0].startswith(
        "http://testserver/cog/tiles/WebMercatorQuad/{z}/{x}/{y}@2x.png?url=https"
    )

    cmap_dict = {
        "1": [58, 102, 24, 255],
        "2": [100, 177, 41],
        "3": "#b1b129",
        "4": "#ddcb9aFF",
    }
    cmap = urlencode({"colormap": json.dumps(cmap_dict)})
    response = app.get(
        f"/cog/tilejson.json?url=https://myurl.com/above_cog.tif&bidx=1&{cmap}"
    )
    assert response.status_code == 200
    body = response.json()
    assert body["tiles"][0].startswith(
        "http://testserver/cog/tiles/WebMercatorQuad/{z}/{x}/{y}@1x?url=https"
    )
    query = dict(parse_qsl(urlparse(body["tiles"][0]).query))
    assert json.loads(query["colormap"]) == cmap_dict