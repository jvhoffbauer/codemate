@router.put(
    "/{user_id}",
    response_model=schemas.User,
    dependencies=[Depends(deps.get_current_active_superuser)],
)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    user: models.User = Depends(get_user),
    user_in: schemas.UserUpdate,
):
    """Update a user."""
    return crud.user.update(db, db_obj=user, obj_in=user_in)