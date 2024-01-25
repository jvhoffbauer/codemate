@needs_py39
# TODO: pv2 add version with Pydantic v2
@needs_pydanticv1
def test_read_items(client):
    response = client.get("/items/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data
    first_item = data[0]
    assert "title" in first_item
    assert "description" in first_item