def test_tuple_form_valid():
    response = client.post("/tuple-form/", data={"values": ("1", "2")})
    assert response.status_code == 200, response.text
    assert response.json() == [1, 2]