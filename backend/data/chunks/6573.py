def test_save(tmp_path, name, content, kwargs):
    test_path = tmp_path / name
    assert not test_path.exists()

    result = app.io.save(test_path, content, **kwargs)
    assert result == test_path
    assert test_path.exists()