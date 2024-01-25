def get_superuser_auth_header(client: TestClient) -> dict[str, str]:
    return get_auth_header(
        client=client,
        email=settings.FIRST_SUPERUSER,
        password=settings.FIRST_SUPERUSER_PASSWORD,
    )