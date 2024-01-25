def test_cog_viewer(app):
    """Test COG Viewer."""
    response = app.get("/cog/viewer", headers={"accept-encoding": "gzip"})
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert response.headers["content-encoding"] == "gzip"