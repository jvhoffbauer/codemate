def test_call_api():
    app = create_app()
    client = TestClient(app)
    response = client.post("/schema_extra/", json={"data": "Foo"})
    assert response.status_code == 200, response.text
    response = client.post("/example/", json={"data": "Foo"})
    assert response.status_code == 200, response.text
    response = client.post("/examples/", json={"data": "Foo"})
    assert response.status_code == 200, response.text
    response = client.post("/example_examples/", json={"data": "Foo"})
    assert response.status_code == 200, response.text
    response = client.get("/path_example/foo")
    assert response.status_code == 200, response.text
    response = client.get("/path_examples/foo")
    assert response.status_code == 200, response.text
    response = client.get("/path_example_examples/foo")
    assert response.status_code == 200, response.text
    response = client.get("/query_example/")
    assert response.status_code == 200, response.text
    response = client.get("/query_examples/")
    assert response.status_code == 200, response.text
    response = client.get("/query_example_examples/")
    assert response.status_code == 200, response.text
    response = client.get("/header_example/")
    assert response.status_code == 200, response.text
    response = client.get("/header_examples/")
    assert response.status_code == 200, response.text
    response = client.get("/header_example_examples/")
    assert response.status_code == 200, response.text
    response = client.get("/cookie_example/")
    assert response.status_code == 200, response.text
    response = client.get("/cookie_examples/")
    assert response.status_code == 200, response.text
    response = client.get("/cookie_example_examples/")
    assert response.status_code == 200, response.text