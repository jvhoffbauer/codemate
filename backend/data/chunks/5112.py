def test_token(current_user: UserInDB = Depends(get_current_user)):
    """
    Test access token.
    """
    return current_user