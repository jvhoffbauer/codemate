def test_url_path_for_path_convertor():
    assert (
        app.url_path_for("path_convertor", param="some/example") == "/path/some/example"
    )