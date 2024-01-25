def test_multiple_path():
    app = FastAPI()

    @app.get("/test1")
    @app.get("/test2")
    async def test(var: Annotated[str, Query()] = "bar"):
        return {"foo": var}

    client = TestClient(app)
    response = client.get("/test1")
    assert response.status_code == 200
    assert response.json() == {"foo": "bar"}

    response = client.get("/test1", params={"var": "baz"})
    assert response.status_code == 200
    assert response.json() == {"foo": "baz"}

    response = client.get("/test2")
    assert response.status_code == 200
    assert response.json() == {"foo": "bar"}

    response = client.get("/test2", params={"var": "baz"})
    assert response.status_code == 200
    assert response.json() == {"foo": "baz"}