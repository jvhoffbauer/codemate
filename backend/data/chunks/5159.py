def test_update_item():
    title = random_lower_string()
    description = random_lower_string()
    id = crud.utils.generate_new_id()
    item_in = ItemCreate(title=title, description=description)
    bucket = get_default_bucket()
    user = create_random_user()
    item = crud.item.upsert(
        bucket=bucket, id=id, doc_in=item_in, owner_username=user.username, persist_to=1
    )
    description2 = random_lower_string()
    item_update = ItemUpdate(description=description2)
    item2 = crud.item.update(
        bucket=bucket,
        id=id,
        doc_in=item_update,
        owner_username=item.owner_username,
        persist_to=1,
    )
    assert item.id == item2.id
    assert item.title == item2.title
    assert item.description == description
    assert item2.description == description2
    assert item.owner_username == item2.owner_username