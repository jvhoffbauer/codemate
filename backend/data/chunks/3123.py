@pytest.mark.parametrize(
    "url,status_code,expected",
    [
        (
            "/main-depends/",
            200,
            {"in": "main-depends", "params": {"q": None, "skip": 5, "limit": 10}},
        ),
        (
            "/main-depends/?q=foo",
            200,
            {"in": "main-depends", "params": {"q": "foo", "skip": 5, "limit": 10}},
        ),
        (
            "/main-depends/?q=foo&skip=100&limit=200",
            200,
            {"in": "main-depends", "params": {"q": "foo", "skip": 5, "limit": 10}},
        ),
        ("/decorator-depends/", 200, {"in": "decorator-depends"}),
        (
            "/router-depends/",
            200,
            {"in": "router-depends", "params": {"q": None, "skip": 5, "limit": 10}},
        ),
        (
            "/router-depends/?q=foo",
            200,
            {"in": "router-depends", "params": {"q": "foo", "skip": 5, "limit": 10}},
        ),
        (
            "/router-depends/?q=foo&skip=100&limit=200",
            200,
            {"in": "router-depends", "params": {"q": "foo", "skip": 5, "limit": 10}},
        ),
        ("/router-decorator-depends/", 200, {"in": "router-decorator-depends"}),
    ],
)
def test_override_simple(url, status_code, expected):
    app.dependency_overrides[common_parameters] = overrider_dependency_simple
    response = client.get(url)
    assert response.status_code == status_code
    assert response.json() == expected
    app.dependency_overrides = {}