def test_create_item_with_sub():
    client = get_app_client()
    client_no = get_app_client(separate_input_output_schemas=False)
    data = {
        "name": "Plumbus",
        "sub": {"subname": "SubPlumbus", "sub_description": "Sub WTF"},
    }
    response = client.post("/items/", json=data)
    response2 = client_no.post("/items/", json=data)
    assert response.status_code == response2.status_code == 200, response.text
    assert (
        response.json()
        == response2.json()
        == {
            "name": "Plumbus",
            "description": None,
            "sub": {"subname": "SubPlumbus", "sub_description": "Sub WTF", "tags": []},
        }
    )