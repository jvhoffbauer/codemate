def test_algo():
    """test algorithm deps."""

    from titiler.core.algorithm import algorithms as default_algorithms

    PostProcessParams = default_algorithms.dependency

    app = FastAPI()

    @app.get("/")
    def _endpoint(algorithm=Depends(PostProcessParams)):
        """return params."""
        if algorithm:
            return algorithm.dict()
        return {}

    client = TestClient(app)
    response = client.get("/")
    assert not response.json()

    response = client.get("/?algorithm=hillshad")
    assert response.status_code == 422

    response = client.get("/?algorithm=hillshade")
    assert response.json()["azimuth"] == 90
    assert response.json()["buffer"] == 3
    assert response.json()["input_nbands"] == 1

    response = client.get(
        "/",
        params={
            "algorithm": "hillshade",
            "algorithm_params": json.dumps({"azimuth": 30, "buffer": 4}),
        },
    )
    assert response.json()["azimuth"] == 30
    assert response.json()["buffer"] == 4
    assert response.json()["input_nbands"] == 1