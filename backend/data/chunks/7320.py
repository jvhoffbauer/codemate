@router.get(
    "/{user_id}",
    response_model=schemas.User,
    dependencies=[Depends(deps.get_current_active_superuser)],
)
def read_user_by_id(user: models.User = Depends(get_user)):
    """Get a specific user by id."""
    return user