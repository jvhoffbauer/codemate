def test_override_with_sub_router_depends_k_bar():
    app.dependency_overrides[common_parameters] = overrider_dependency_with_sub
    response = client.get("/router-depends/?k=bar")
    assert response.status_code == 200
    assert response.json() == {"in": "router-depends", "params": {"k": "bar"}}
    app.dependency_overrides = {}