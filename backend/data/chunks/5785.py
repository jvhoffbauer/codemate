def test_validate(app):
    """test POST /mosaicjson/validate endpoint"""
    body = read_json_fixture("mosaic.json")
    response = app.post("/mosaicjson/validate", json=body)
    assert response.status_code == 200

    response = app.post("/mosaicjson/validate", json={"nope": "oups"})
    assert response.status_code == 422