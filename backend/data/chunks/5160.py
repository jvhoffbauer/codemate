def test_delete_item():
    title = random_lower_string()
    description = random_lower_string()
    id = crud.utils.generate_new_id()
    item_in = ItemCreate(title=title, description=description)
    bucket = get_default_bucket()
    user = create_random_user()
    item = crud.item.upsert(
        bucket=bucket, id=id, doc_in=item_in, owner_username=user.username, persist_to=1
    )
    item2 = crud.item.remove(bucket=bucket, id=id, persist_to=1)
    item3 = crud.item.get(bucket=bucket, id=id)
    assert item3 is None
    assert item2.id == id
    assert item2.title == title
    assert item2.description == description
    assert item2.owner_username == user.username