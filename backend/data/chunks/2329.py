def test_complex():
    app = FastAPI()

    @app.post("/")
    def foo(foo: Union[str, List[int]]):
        return foo

    client = TestClient(app)

    response = client.post("/", json="bar")
    assert response.status_code == 200, response.text
    assert response.json() == "bar"

    response2 = client.post("/", json=[1, 2])
    assert response2.status_code == 200, response2.text
    assert response2.json() == [1, 2]