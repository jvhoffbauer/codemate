def delete_item(
    *,
    db: Session = Depends(deps.get_db),
    item: models.Item = Depends(get_item),
    user: models.User = Depends(deps.get_current_active_user),
):
    """Delete an item."""
    if not crud.user.is_superuser(user) and (item.owner_id != user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    item = crud.item.remove(db=db, id=item.id)
    return item