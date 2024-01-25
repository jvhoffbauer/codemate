@pytest.mark.parametrize(*IO_PARAMS)
def test_round_trip(tmp_path, name, content, kwargs):
    test_path = tmp_path / name
    assert not test_path.exists()

    app.io.save(test_path, content, **kwargs)
    assert app.io.load(test_path) == content