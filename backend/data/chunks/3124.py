def test_override_simple(url, status_code, expected):
    app.dependency_overrides[common_parameters] = overrider_dependency_simple
    response = client.get(url)
    assert response.status_code == status_code
    assert response.json() == expected
    app.dependency_overrides = {}