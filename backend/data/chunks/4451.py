def test_normal_app():
    from docs_src.dependency_testing.tutorial001_an_py310 import app, client

    app.dependency_overrides = None
    response = client.get("/items/?q=foo&skip=100&limit=200")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "message": "Hello Items!",
        "params": {"q": "foo", "skip": 100, "limit": 200},
    }