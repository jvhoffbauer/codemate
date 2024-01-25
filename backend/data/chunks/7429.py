def login_access_token(
    *,
    req: sys_user_schema.UserPhoneAuth,
) -> Any:
    """
    简单实现登录
    :param req:
    :return:
    """

    # 验证用户 简短的业务可以写在这里
    # user = User.single_by_phone(phone=req.username)
    # if not user:
    #     return resp.fail(resp.DataNotFound.set_msg("账号或密码错误"))
    #
    # if not security.verify_password(req.password, user.password):
    #     return resp.fail(resp.DataNotFound.set_msg("账号或密码错误"))
    #
    # access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    #
    # # 登录token 存储了user.id
    # return resp.ok(data={
    #     "token": security.create_access_token(user.id, expires_delta=access_token_expires),
    # })

    # 复杂的业务逻辑建议 抽离到 logic文件夹下
    token = UserLogic().user_login_logic(req.username, req.password)
    return resp.ok(data={"token": token})