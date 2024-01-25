def test_point(app):
    """test GET /mosaicjson/point endpoint"""
    mosaicjson = read_json_fixture(MOSAICJSON_FILE)
    center = mosaicjson["center"]
    with patch.object(FileBackend, "_read", mosaic_read_factory(MOSAICJSON_FILE)):
        response = app.get(
            f"/mosaicjson/point/{center[0]},{center[1]}",
            params={"url": MOSAICJSON_FILE},
        )
    assert response.status_code == 200
    body = response.json()
    assert len(body["values"]) == 1
    assert body["values"][0][0].endswith(".tif")
    assert body["values"][0][1] == [9943, 9127, 9603]