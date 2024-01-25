@router.post("/reset-password", response_model=schemas.Msg)
def reset_password(
    *,
    db: Session = Depends(deps.get_db),
    token: str = Body(),
    new_password: str = Body()
):
    email = verify_password_reset_token(token)
    if not email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token."
        )
    user = crud.user.get_by_email(db, email=email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found."
        )
    if not crud.user.is_active(user):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user."
        )
    user.hashed_password = get_password_hash(new_password)
    db.add(user)
    db.commit()
    return {"msg": "Password updated successfully."}