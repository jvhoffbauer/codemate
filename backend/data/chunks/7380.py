def create_random_item(db: Session, owner_id: int | None = None) -> models.Item:
    if owner_id is None:
        user = create_random_user(db)
        owner_id = user.id
    title = random_lower_string()
    description = random_lower_string()
    item_in = schemas.ItemCreate(
        title=title, description=description, owner_id=owner_id
    )
    return crud.item.create_with_owner(db, obj_in=item_in, owner_id=owner_id)