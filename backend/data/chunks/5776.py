def test_read_mosaic(app):
    """test GET /mosaicjson endpoint"""
    # TODO: Remove
    response = app.get("/mosaicjson", params={"url": MOSAICJSON_FILE})
    assert response.status_code == 200
    MosaicJSON(**response.json())

    response = app.get("/mosaicjson/", params={"url": MOSAICJSON_FILE})
    assert response.status_code == 200
    MosaicJSON(**response.json())