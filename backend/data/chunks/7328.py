@router.post("/password-recovery/{email}", response_model=schemas.Msg)
def recover_password(*, db: Session = Depends(deps.get_db), email: EmailStr):
    user = crud.user.get_by_email(db, email=email)
    password_reset_token = generate_password_reset_token(email=email)
    if user:
        send_reset_password_email(
            email_to=user.email, email=email, token=password_reset_token
        )
    return {
        "msg": "If this email is registered within our system, you'll get an recovery email."
    }