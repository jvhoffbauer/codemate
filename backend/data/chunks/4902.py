@needs_py39
def test_post_body_json(client: TestClient):
    response = client.post("/files/", json={"file": "Foo", "token": "Bar"})
    assert response.status_code == 422, response.text
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "missing",
                    "loc": ["body", "file"],
                    "msg": "Field required",
                    "input": None,
                    "url": match_pydantic_error_url("missing"),
                },
                {
                    "type": "missing",
                    "loc": ["body", "fileb"],
                    "msg": "Field required",
                    "input": None,
                    "url": match_pydantic_error_url("missing"),
                },
                {
                    "type": "missing",
                    "loc": ["body", "token"],
                    "msg": "Field required",
                    "input": None,
                    "url": match_pydantic_error_url("missing"),
                },
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "loc": ["body", "file"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
                {
                    "loc": ["body", "fileb"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
                {
                    "loc": ["body", "token"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
            ]
        }
    )