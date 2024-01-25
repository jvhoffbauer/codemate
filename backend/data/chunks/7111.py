@router.get("/{user_id}")
def read_user_by_id(
    user_id: int, session: SessionDep, current_user: CurrentUser
) -> UserOut:
    """
    Get a specific user by id.
    """
    user = session.get(User, user_id)
    if user == current_user:
        return user  # type: ignore
    if not current_user.is_superuser:
        raise HTTPException(
            # TODO: Review status code
            status_code=400,
            detail="The user doesn't have enough privileges",
        )
    return user  # type: ignore