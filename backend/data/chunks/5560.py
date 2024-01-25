def test_lowercase_middleware_multiple_values():
    """Make sure all values are available for lists."""
    app = FastAPI()

    @app.get("/route1")
    async def route1(value: List[str] = Query(...)):
        """route1."""
        return {"value": value}

    app.add_middleware(LowerCaseQueryStringMiddleware)

    client = TestClient(app)

    response = client.get("/route1?value=lorenzori&value=dogs")
    assert response.json() == {"value": ["lorenzori", "dogs"]}

    response = client.get("/route1?VALUE=lorenzori&VALUE=dogs&value=trucks")
    assert response.json() == {"value": ["lorenzori", "dogs", "trucks"]}