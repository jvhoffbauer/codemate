def test_verify_password():
    from docs_src.security.tutorial005_an_py39 import fake_users_db, verify_password

    assert verify_password("secret", fake_users_db["johndoe"]["hashed_password"])