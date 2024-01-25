def get_auth_header(
    *, client: TestClient, email: EmailStr, password: str
) -> dict[str, str]:
    return _get_auth_header_from_credentials(
        client, {"username": email, "password": password}
    )