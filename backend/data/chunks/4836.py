def test_create_access_token():
    access_token = create_access_token(data={"data": "foo"})
    assert access_token