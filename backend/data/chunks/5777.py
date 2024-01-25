def test_bounds(app):
    """test GET /mosaicjson/bounds endpoint"""
    response = app.get("/mosaicjson/bounds", params={"url": MOSAICJSON_FILE})
    assert response.status_code == 200
    body = response.json()
    assert len(body["bounds"]) == 4
    assert body["bounds"][0] < body["bounds"][2]
    assert body["bounds"][1] < body["bounds"][3]