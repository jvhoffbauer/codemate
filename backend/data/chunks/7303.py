@router.patch("/{id}", response_model=schemas.Item)
def update_item(
    *,
    db: Session = Depends(deps.get_db),
    item: models.Item = Depends(get_item),
    item_in: schemas.ItemUpdate,
    user: models.User = Depends(deps.get_current_active_user),
):
    """Update an item."""
    if not crud.user.is_superuser(user) and (item.owner_id != user.id):
        raise HTTPException(status_code=400, detail="This item belongs to another user")
    item = crud.item.update(db=db, db_obj=item, obj_in=item_in)
    return item