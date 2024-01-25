@router.post(
    "/test-email",
    response_model=schemas.Msg,
    status_code=201,
    dependencies=[Depends(deps.get_current_active_superuser)],
)
def test_email(
    email_to: EmailStr,
) -> Any:
    """Test email sending."""
    send_test_email(email_to=email_to)
    return {"msg": "Test email was sent."}