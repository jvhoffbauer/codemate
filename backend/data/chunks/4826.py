def get_access_token(username="johndoe", password="secret", scope=None):
    data = {"username": username, "password": password}
    if scope:
        data["scope"] = scope
    response = client.post("/token", data=data)
    content = response.json()
    access_token = content.get("access_token")
    return access_token