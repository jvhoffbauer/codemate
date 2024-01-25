def test_validate_cog(app, url):
    """test /validate endpoint"""
    response = app.get(f"/cog/validate?url={os.path.join(DATA_DIR, 'cog.tif')}")
    assert response.status_code == 200
    assert response.json()["COG"]