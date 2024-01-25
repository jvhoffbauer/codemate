def test_info(app):
    """test GET /mosaicjson/info endpoint"""
    response = app.get("/mosaicjson/info", params={"url": MOSAICJSON_FILE})
    assert response.status_code == 200
    body = response.json()
    assert body["minzoom"] == 7
    assert body["maxzoom"] == 9
    assert body["name"] == "mosaic"  # mosaic.name is not set
    assert body["quadkeys"] == []

    response = app.get("/mosaicjson/info.geojson", params={"url": MOSAICJSON_FILE})
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/geo+json"
    body = response.json()
    assert body["geometry"]
    assert body["properties"]["minzoom"] == 7
    assert body["properties"]["maxzoom"] == 9
    assert body["properties"]["name"] == "mosaic"  # mosaic.name is not set
    assert body["properties"]["quadkeys"] == []