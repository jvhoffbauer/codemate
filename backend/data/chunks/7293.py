def get_current_active_superuser(
    current_active_user: models.User = Depends(get_current_active_user),
) -> models.User:
    if not crud.user.is_superuser(current_active_user):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user doesn't have enough privileges.",
        )
    return current_active_user