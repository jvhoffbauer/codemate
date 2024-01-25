def test_call_api():
    response = client.post("/examples/", json={"data": "example1"})
    assert response.status_code == 200, response.text

    response = client.get("/path_examples/foo")
    assert response.status_code == 200, response.text

    response = client.get("/query_examples/")
    assert response.status_code == 200, response.text

    response = client.get("/header_examples/")
    assert response.status_code == 200, response.text

    response = client.get("/cookie_examples/")
    assert response.status_code == 200, response.text