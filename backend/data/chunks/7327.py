def test_token(current_user: models.User = Depends(deps.get_current_active_user)):
    """
    Test access token
    """
    return current_user