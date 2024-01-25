def normal_user_token_headers(client: TestClient, db: Session) -> dict[str, str]:
    return get_auth_header_from_email(
        client=client, db=db, email=settings.EMAIL_TEST_USER
    )