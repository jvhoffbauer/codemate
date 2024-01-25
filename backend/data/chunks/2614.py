def test_tuple_form_invalid():
    response = client.post("/tuple-form/", data={"values": ("1", "2", "3")})
    assert response.status_code == 422, response.text

    response = client.post("/tuple-form/", data={"values": ("1")})
    assert response.status_code == 422, response.text