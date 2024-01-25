def test_no_duplicates():
    response = client.post(
        "/no-duplicates",
        json={"item": {"data": "myitem"}, "item2": {"data": "myitem2"}},
    )
    assert response.status_code == 200, response.text
    assert response.json() == [{"data": "myitem"}, {"data": "myitem2"}]