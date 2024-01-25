def test_bdix():
    """test bidx deps."""

    app = FastAPI()

    @app.get("/first")
    def _bidx(params=Depends(dependencies.BidxParams)):
        """return indexes."""
        return params.indexes

    @app.get("/second")
    def _bidx_expr(params=Depends(dependencies.BidxExprParams)):
        """return params."""
        return params

    @app.get("/third")
    def _expre(params=Depends(dependencies.ExpressionParams)):
        """return express."""
        return params.expression

    client = TestClient(app)
    response = client.get("/first?bidx=1&bidx=2")
    assert response.json() == [1, 2]

    response = client.get("/first")
    assert not response.json()

    response = client.get("/second?bidx=1&bidx=2")
    assert response.json()["indexes"] == [1, 2]

    response = client.get("/second", params={"expression": "1;2"})
    assert response.json()["expression"] == "1;2"

    response = client.get("/second")
    assert not response.json()["expression"]
    assert not response.json()["indexes"]

    response = client.get("/third", params={"expression": "1;2"})
    assert response.json() == "1;2"

    response = client.get("/third")
    assert not response.json()