def test_override_with_sub_main_depends_k_bar():
    app.dependency_overrides[common_parameters] = overrider_dependency_with_sub
    response = client.get("/main-depends/?k=bar")
    assert response.status_code == 200
    assert response.json() == {"in": "main-depends", "params": {"k": "bar"}}
    app.dependency_overrides = {}