def superuser_token_headers(client: TestClient) -> dict[str, str]:
    return get_superuser_auth_header(client)