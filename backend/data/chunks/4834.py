def test_verify_password():
    assert verify_password("secret", fake_users_db["johndoe"]["hashed_password"])