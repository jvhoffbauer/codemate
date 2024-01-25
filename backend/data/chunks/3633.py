def test_q_fixedquery():
    client = get_client()
    response = client.post("/items/", data={"q": "fixedquery"})
    assert response.status_code == 200
    assert response.json() == "Hello fixedquery"