def test_assets():
    """test assets deps."""

    app = FastAPI()

    @app.get("/first")
    def _assets(params=Depends(dependencies.AssetsParams)):
        """return assets."""
        return params.assets

    @app.get("/second")
    def _assets_expr(params=Depends(dependencies.AssetsBidxExprParams)):
        """return params."""
        return params

    @app.get("/third")
    def _assets_bidx(params=Depends(dependencies.AssetsBidxParams)):
        """return params."""
        return params

    client = TestClient(app)
    response = client.get("/first?assets=data&assets=image")
    assert response.json() == ["data", "image"]

    response = client.get("/first")
    assert not response.json()

    response = client.get("/second?assets=data&assets=image")
    assert response.json()["assets"] == ["data", "image"]
    assert not response.json()["expression"]

    response = client.get("/second?expression=data*image")
    assert response.json()["expression"] == "data*image"
    assert not response.json()["assets"]

    with pytest.raises(errors.MissingAssets):
        response = client.get("/second")

    response = client.get(
        "/second?assets=data&assets=image&asset_bidx=data|1,2,3&asset_bidx=image|1"
    )
    assert response.json()["assets"] == ["data", "image"]
    assert response.json()["asset_indexes"] == {"data": [1, 2, 3], "image": [1]}

    response = client.get("/third?assets=data&assets=image")
    assert response.json()["assets"] == ["data", "image"]

    response = client.get("/third")
    assert not response.json()["assets"]

    response = client.get(
        "/third?assets=data&assets=image&asset_bidx=data|1,2,3&asset_bidx=image|1"
    )
    assert response.json()["assets"] == ["data", "image"]
    assert response.json()["asset_indexes"] == {"data": [1, 2, 3], "image": [1]}

    response = client.get(
        "/third?assets=data&assets=image&asset_expression=data|b1\b2&asset_expression=image|b1*b2"
    )
    assert response.json()["assets"] == ["data", "image"]
    assert response.json()["asset_expression"] == {"data": "b1\b2", "image": "b1*b2"}