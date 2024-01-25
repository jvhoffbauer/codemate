def test_get_portal():
    response = client.get("/portal")
    assert response.status_code == 200, response.text
    assert response.json() == {"message": "Here's your interdimensional portal."}