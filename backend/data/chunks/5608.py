def test_image():
    """test image deps."""

    app = FastAPI()

    @app.get("/")
    def _endpoint(params=Depends(dependencies.ImageParams)):
        """return params."""
        return params

    client = TestClient(app)
    response = client.get("/")
    assert response.json()["max_size"] == 1024
    assert not response.json()["height"]
    assert not response.json()["width"]

    response = client.get("/?max_size=2048")
    assert response.json()["max_size"] == 2048
    assert not response.json()["height"]
    assert not response.json()["width"]

    response = client.get("/?width=128")
    assert response.json()["max_size"] == 1024
    assert not response.json()["height"]
    assert response.json()["width"] == 128

    response = client.get("/?width=128&height=128")
    assert not response.json()["max_size"]
    assert response.json()["height"] == 128
    assert response.json()["width"] == 128