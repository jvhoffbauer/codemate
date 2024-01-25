def test_extra_types(client: TestClient):
    item_id = "ff97dd87-a4a5-4a12-b412-cde99f33e00e"
    data = {
        "start_datetime": "2018-12-22T14:00:00+00:00",
        "end_datetime": "2018-12-24T15:00:00+00:00",
        "repeat_at": "15:30:00",
        "process_after": 300,
    }
    expected_response = data.copy()
    expected_response.update(
        {
            "start_process": "2018-12-22T14:05:00+00:00",
            "duration": 176_100,
            "item_id": item_id,
        }
    )
    response = client.put(f"/items/{item_id}", json=data)
    assert response.status_code == 200, response.text
    assert response.json() == expected_response