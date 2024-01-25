def test_dependency_no_exception():
    assert state["except"] is False
    assert state["finally"] is False
    response = client.put("/user/rick", json="Morty")
    assert response.status_code == 200, response.text
    assert response.json() == {"message": "OK"}
    assert state["except"] is False
    assert state["finally"] is True
    assert fake_database["rick"] == "Morty"