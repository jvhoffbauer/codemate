def _get_auth_header_from_credentials(
    client: TestClient,
    login_data: dict[str, str],
) -> dict[str, str]:
    response = client.post(settings.API_LOGIN_STR, data=login_data)
    tokens = response.json()
    access_token = tokens["access_token"]
    return {"Authorization": f"Bearer {access_token}"}