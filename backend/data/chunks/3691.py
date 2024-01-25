def test_create_item_list():
    client = get_app_client()
    client_no = get_app_client(separate_input_output_schemas=False)
    data = [
        {"name": "Plumbus"},
        {
            "name": "Portal Gun",
            "description": "Device to travel through the multi-rick-verse",
        },
    ]
    response = client.post("/items-list/", json=data)
    response2 = client_no.post("/items-list/", json=data)
    assert response.status_code == response2.status_code == 200, response.text
    assert (
        response.json()
        == response2.json()
        == [
            {"name": "Plumbus", "description": None, "sub": None},
            {
                "name": "Portal Gun",
                "description": "Device to travel through the multi-rick-verse",
                "sub": None,
            },
        ]
    )