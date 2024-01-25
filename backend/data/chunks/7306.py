def read_item(
    *,
    item: models.Item = Depends(get_item),
    user: models.User = Depends(deps.get_current_active_user),
):
    """Get item by id."""
    if not crud.user.is_superuser(user) and (item.owner_id != user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions.")
    return item