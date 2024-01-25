@pytest.mark.parametrize(
    "url",
    [os.path.join(DATA_DIR, f) for f in os.listdir(DATA_DIR) if f.endswith(".tif")],
)
def test_validate_cog(app, url):
    """test /validate endpoint"""
    response = app.get(f"/cog/validate?url={os.path.join(DATA_DIR, 'cog.tif')}")
    assert response.status_code == 200
    assert response.json()["COG"]