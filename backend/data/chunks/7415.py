def get_current_user(token: Optional[str] = Depends(check_jwt_token)) -> User:
    """
    根据header中token 获取当前用户
    :param db:
    :param token:
    :return:
    """
    user = User.single_by_id(uid=token.get("sub"))
    if not user:
        raise custom_exc.TokenAuthError(err_desc="User not found")
    return user