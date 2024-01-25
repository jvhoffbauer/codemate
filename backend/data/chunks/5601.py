def test_bands():
    """test bands deps."""

    app = FastAPI()

    @app.get("/first")
    def _bands(params=Depends(dependencies.BandsParams)):
        """return bands."""
        return params.bands

    @app.get("/second")
    def _bands_expr(params=Depends(dependencies.BandsExprParams)):
        """return params."""
        return params

    @app.get("/third")
    def _bands_expr_opt(params=Depends(dependencies.BandsExprParamsOptional)):
        """return params."""
        return params

    client = TestClient(app)
    response = client.get("/first?bands=b1&bands=b2")
    assert response.json() == ["b1", "b2"]

    response = client.get("/first")
    assert not response.json()

    response = client.get("/second?bands=b1&bands=b2")
    assert response.json()["bands"] == ["b1", "b2"]

    response = client.get("/second", params={"expression": "b1;b2"})
    assert response.json()["expression"] == "b1;b2"

    with pytest.raises(errors.MissingBands):
        response = client.get("/second")

    response = client.get("/third?bands=b1&bands=b2")
    assert response.json()["bands"] == ["b1", "b2"]

    response = client.get("/third", params={"expression": "b1;b2"})
    assert response.json()["expression"] == "b1;b2"

    response = client.get("/third")
    assert not response.json()["bands"]