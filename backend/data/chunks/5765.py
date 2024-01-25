def test_file_not_found_error(app):
    """raise 404 when file is not found."""
    response = app.get("/cog/info?url=foo.tif")
    assert response.status_code == 500