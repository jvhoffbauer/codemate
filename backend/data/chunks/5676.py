def test_algorithm():
    """Test Algorithms endpoint."""
    algorithm = AlgorithmFactory()

    app = FastAPI()
    app.include_router(algorithm.router)
    client = TestClient(app)

    response = client.get("/algorithms")
    assert response.status_code == 200
    assert "hillshade" in response.json()

    response = client.get("/algorithms/hillshade")
    assert response.status_code == 200