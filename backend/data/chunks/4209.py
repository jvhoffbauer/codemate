@needs_py310
def test_wrong_headers(client: TestClient):
    data = '{"name": "Foo", "price": 50.5}'
    response = client.post(
        "/items/", content=data, headers={"Content-Type": "text/plain"}
    )
    assert response.status_code == 422, response.text
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "model_attributes_type",
                    "loc": ["body"],
                    "msg": "Input should be a valid dictionary or object to extract fields from",
                    "input": '{"name": "Foo", "price": 50.5}',
                    "url": match_pydantic_error_url("model_attributes_type"),
                }
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "loc": ["body"],
                    "msg": "value is not a valid dict",
                    "type": "type_error.dict",
                }
            ]
        }
    )

    response = client.post(
        "/items/", content=data, headers={"Content-Type": "application/geo+json-seq"}
    )
    assert response.status_code == 422, response.text
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "model_attributes_type",
                    "loc": ["body"],
                    "msg": "Input should be a valid dictionary or object to extract fields from",
                    "input": '{"name": "Foo", "price": 50.5}',
                    "url": match_pydantic_error_url("model_attributes_type"),
                }
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "loc": ["body"],
                    "msg": "value is not a valid dict",
                    "type": "type_error.dict",
                }
            ]
        }
    )
    response = client.post(
        "/items/", content=data, headers={"Content-Type": "application/not-really-json"}
    )
    assert response.status_code == 422, response.text
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "model_attributes_type",
                    "loc": ["body"],
                    "msg": "Input should be a valid dictionary or object to extract fields from",
                    "input": '{"name": "Foo", "price": 50.5}',
                    "url": match_pydantic_error_url("model_attributes_type"),
                }
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "loc": ["body"],
                    "msg": "value is not a valid dict",
                    "type": "type_error.dict",
                }
            ]
        }
    )