@needs_py39
# TODO: pv2 add version with Pydantic v2
@needs_pydanticv1
def test_inexistent_user(client):
    response = client.get("/users/999")
    assert response.status_code == 404, response.text