def test_create_item():
    title = random_lower_string()
    description = random_lower_string()
    id = crud.utils.generate_new_id()
    item_in = ItemCreate(title=title, description=description)
    bucket = get_default_bucket()
    user = create_random_user()
    item = crud.item.upsert(
        bucket=bucket, id=id, doc_in=item_in, owner_username=user.username, persist_to=1
    )
    assert item.id == id
    assert item.type == ITEM_DOC_TYPE
    assert item.title == title
    assert item.description == description
    assert item.owner_username == user.username