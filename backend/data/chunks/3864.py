@needs_py39
# TODO: pv2 add Pydantic v2 version
@needs_pydanticv1
def test_create_item(client):
    item = {"title": "Foo", "description": "Something that fights"}
    response = client.post("/users/1/items/", json=item)
    assert response.status_code == 200, response.text
    item_data = response.json()
    assert item["title"] == item_data["title"]
    assert item["description"] == item_data["description"]
    assert "id" in item_data
    assert "owner_id" in item_data
    response = client.get("/users/1")
    assert response.status_code == 200, response.text
    user_data = response.json()
    item_to_check = [it for it in user_data["items"] if it["id"] == item_data["id"]][0]
    assert item_to_check["title"] == item["title"]
    assert item_to_check["description"] == item["description"]
    response = client.get("/users/1")
    assert response.status_code == 200, response.text
    user_data = response.json()
    item_to_check = [it for it in user_data["items"] if it["id"] == item_data["id"]][0]
    assert item_to_check["title"] == item["title"]
    assert item_to_check["description"] == item["description"]