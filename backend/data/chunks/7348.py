def generate_password_reset_token(email: EmailStr) -> str:
    return create_access_token(
        subject=email,
        expires_delta=timedelta(hours=settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS),
    )