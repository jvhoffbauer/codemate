def update_user_me(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserUpdate,
    user: models.User = Depends(deps.get_current_active_user),
):
    """Update own user."""
    return crud.user.update(db, db_obj=user, obj_in=user_in)