def test_email(
    email_to: EmailStr,
) -> Any:
    """Test email sending."""
    send_test_email(email_to=email_to)
    return {"msg": "Test email was sent."}