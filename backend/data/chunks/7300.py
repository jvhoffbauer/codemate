def read_items(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    user: models.User = Depends(deps.get_current_active_user),
):
    """Retrieve items."""
    if crud.user.is_superuser(user):
        items = crud.item.get_multi(db, skip=skip, limit=limit)
    else:
        items = crud.item.get_multi_by_owner(
            db, owner_id=user.id, skip=skip, limit=limit
        )
    return items