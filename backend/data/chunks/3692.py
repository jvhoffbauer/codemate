def test_read_items():
    client = get_app_client()
    client_no = get_app_client(separate_input_output_schemas=False)
    response = client.get("/items/")
    response2 = client_no.get("/items/")
    assert response.status_code == response2.status_code == 200, response.text
    assert (
        response.json()
        == response2.json()
        == [
            {
                "name": "Portal Gun",
                "description": "Device to travel through the multi-rick-verse",
                "sub": {"subname": "subname", "sub_description": None, "tags": []},
            },
            {"name": "Plumbus", "description": None, "sub": None},
        ]
    )