def test_create_item():
    client = get_app_client()
    client_no = get_app_client(separate_input_output_schemas=False)
    response = client.post("/items/", json={"name": "Plumbus"})
    response2 = client_no.post("/items/", json={"name": "Plumbus"})
    assert response.status_code == response2.status_code == 200, response.text
    assert (
        response.json()
        == response2.json()
        == {"name": "Plumbus", "description": None, "sub": None}
    )