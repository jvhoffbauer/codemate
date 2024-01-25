@router.post(
    "",
    response_model=schemas.User,
    dependencies=[Depends(deps.get_current_active_superuser)],
)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserAdminCreate,
):
    """Create new user."""
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user with this username already exists in the system.",
        )
    user = crud.user.create(db, obj_in=user_in)
    if settings.EMAILS_ENABLED and user_in.email:
        send_new_account_email(email_to=user_in.email, username=user_in.email)
    return user