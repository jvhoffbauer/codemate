def read_user_me(session: SessionDep, current_user: CurrentUser) -> UserOut:
    """
    Get current user.
    """
    return current_user  # type: ignore