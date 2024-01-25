@pytest.fixture(scope="session")
def staff_client(staff: Staff):
    client = ApiClient(app, staff)
    token = gen_jwt('{"admin":1}', 60 * 24)
    client.headers.update({"Authorization": f"Bearer {token}"})
    return client