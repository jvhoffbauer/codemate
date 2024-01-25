def test_algo():
    """test algorithm deps."""
    # Add the `Multiply` algorithm to the default ones
    algorithms = default_algorithms.register({"multiply": Multiply})

    app = FastAPI()

    arr = numpy.random.randint(0, 3000, (3, 256, 256))

    @app.get("/")
    def main(algorithm=Depends(algorithms.dependency)):
        """endpoint."""
        img = ImageData(arr)
        if algorithm:
            return algorithm(img).data.max().tolist()

        return img.data.max().tolist()

    client = TestClient(app)
    response = client.get("/")
    assert response.json() == arr.max().tolist()

    # Missing factor input
    response = client.get("/", params={"algorithm": "multiply"})
    assert response.status_code == 400

    response = client.get(
        "/",
        params={"algorithm": "multiply", "algorithm_params": json.dumps({"factor": 3})},
    )
    assert response.json() == arr.max().tolist() * 3