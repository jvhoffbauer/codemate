def test_render():
    """test render deps."""

    app = FastAPI()

    @app.get("/")
    def _endpoint(params=Depends(dependencies.ImageRenderingParams)):
        """return params."""
        return params

    client = TestClient(app)
    response = client.get("/")
    assert response.json()["add_mask"] is True

    response = client.get("/?return_mask=False")
    assert response.json()["add_mask"] is False

    response = client.get("/?return_mask=True")
    assert response.json()["add_mask"] is True