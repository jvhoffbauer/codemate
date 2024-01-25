def test_tms():
    """Create App."""
    app = FastAPI()

    @app.get("/web/{TileMatrixSetId}")
    def web(TileMatrixSetId: Literal["WebMercatorQuad"] = Query(...)):
        """return tms id."""
        return TileMatrixSetId

    @app.get("/all/{TileMatrixSetId}")
    def all(TileMatrixSetId: Literal[tuple(tms.list())] = Query(...)):
        """return tms id."""
        return TileMatrixSetId

    client = TestClient(app)
    response = client.get("/web/WebMercatorQuad")
    assert response.json() == "WebMercatorQuad"

    response = client.get("/web/WorldCRS84Quad")
    assert response.status_code == 422
    assert "permitted: 'WebMercatorQuad'" in response.json()["detail"][0]["msg"]

    response = client.get("/all/WebMercatorQuad")
    assert response.json() == "WebMercatorQuad"

    response = client.get("/all/WorldCRS84Quad")
    assert response.json() == "WorldCRS84Quad"