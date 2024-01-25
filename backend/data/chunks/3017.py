def test_schema():
    response = client.get("/openapi.json")
    assert response.status_code == status.HTTP_200_OK
    actual_schema = response.json()
    assert actual_schema == schema
    assert (
        len(actual_schema["paths"]["/"]["get"]["parameters"]) == 1
    )  # primary goal of this test