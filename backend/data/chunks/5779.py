def test_tilejson(app):
    """test GET /mosaicjson/tilejson.json endpoint"""
    mosaicjson = read_json_fixture(MOSAICJSON_FILE)
    response = app.get("/mosaicjson/tilejson.json", params={"url": MOSAICJSON_FILE})
    assert response.status_code == 200
    body = response.json()
    TileJSON(**body)

    assert (
        "http://testserver/mosaicjson/tiles/WebMercatorQuad/{z}/{x}/{y}@1x?url="
        in body["tiles"][0]
    )
    assert body["minzoom"] == mosaicjson["minzoom"]
    assert body["maxzoom"] == mosaicjson["maxzoom"]
    assert body["bounds"] == mosaicjson["bounds"]
    assert body["center"] == mosaicjson["center"]