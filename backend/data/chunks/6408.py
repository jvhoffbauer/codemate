async def test_register_crud(async_client: AsyncClient):
    response = await async_client.get("/openapi.json")
    # test paths
    paths = response.json()["paths"]
    assert "/User/list" in paths
    assert "/User/item" in paths
    assert "/User/item/{item_id}" in paths
    assert "/Tag/list" in paths
    assert "/Tag/item" in paths
    assert "/Tag/item/{item_id}" in paths

    # test schemas
    schemas = response.json()["components"]["schemas"]
    # assert "UserSchema" in schemas
    assert "UserFilter" in schemas
    assert "UserList" in schemas
    assert "UserUpdate" in schemas
    assert "ItemListSchema_UserList_" in schemas
    assert "TagFilter" in schemas
    assert "TagList" in schemas
    assert "TagUpdate" in schemas