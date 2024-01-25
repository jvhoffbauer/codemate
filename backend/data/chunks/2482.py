def test_level1_default():
    response = client.get("/default1?level1=foo")
    assert response.json() == "foo"
    assert response.headers["content-type"] == "application/x-level-0"
    assert "x-level0" in response.headers
    assert "x-level1" not in response.headers
    assert "x-level2" not in response.headers
    assert "x-level3" not in response.headers
    assert "x-level4" not in response.headers
    assert "x-level5" not in response.headers