def test_put_correct_body():
    response = client.post("/items/", json=[{"name": "Foo", "age": 5}])
    assert response.status_code == 200, response.text
    assert response.json() == {
        "item": [
            {
                "name": "Foo",
                "age": IsOneOf(
                    5,
                    # TODO: remove when deprecating Pydantic v1
                    "5",
                ),
            }
        ]
    }