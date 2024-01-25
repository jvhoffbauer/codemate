def test_dependency_gets_exception():
    assert state["except"] is False
    assert state["finally"] is False
    response = client.put("/invalid-user/rick", json="Morty")
    assert response.status_code == 400, response.text
    assert response.json() == {"detail": "Invalid user"}
    assert state["except"] is True
    assert state["finally"] is True
    assert fake_database["rick"] == "Rick Sanchez"