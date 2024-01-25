def test_get_item():
    title = random_lower_string()
    description = random_lower_string()
    id = crud.utils.generate_new_id()
    item_in = ItemCreate(title=title, description=description)
    bucket = get_default_bucket()
    user = create_random_user()
    item = crud.item.upsert(
        bucket=bucket, id=id, doc_in=item_in, owner_username=user.username, persist_to=1
    )
    stored_item = crud.item.get(bucket=bucket, id=id)
    assert item.id == stored_item.id
    assert item.title == stored_item.title
    assert item.description == stored_item.description
    assert item.owner_username == stored_item.owner_username