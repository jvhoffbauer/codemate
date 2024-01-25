@patch("rio_tiler.io.rasterio.rasterio")
@patch("rio_tiler.io.stac.httpx")
def test_tilejson(httpx, rio, app):
    """test /tilejson endpoint."""
    httpx.get = mock_RequestGet
    rio.open = mock_rasterio_open

    response = app.get("/stac/tilejson.json?url=https://myurl.com/item.json")
    assert response.status_code == 400

    response = app.get(
        "/stac/tilejson.json?url=https://myurl.com/item.json&assets=B01&minzoom=5&maxzoom=10"
    )
    assert response.status_code == 200
    body = response.json()
    assert body["tilejson"] == "2.2.0"
    assert body["version"] == "1.0.0"
    assert body["scheme"] == "xyz"
    assert len(body["tiles"]) == 1
    assert body["tiles"][0].startswith(
        "http://testserver/stac/tiles/WebMercatorQuad/{z}/{x}/{y}@1x?url="
    )
    assert body["minzoom"] == 5
    assert body["maxzoom"] == 10
    assert body["bounds"]
    assert body["center"]

    response = app.get(
        "/stac/tilejson.json?url=https://myurl.com/item.json&assets=B01&tile_format=png&tile_scale=2"
    )
    assert response.status_code == 200
    body = response.json()
    assert body["tiles"][0].startswith(
        "http://testserver/stac/tiles/WebMercatorQuad/{z}/{x}/{y}@2x.png?url="
    )