    def user_login_logic(phone: int, password: str):
        user = User.single_by_phone(phone=phone)
        if not user:
            raise custom_exc.TokenAuthError(err_desc="账号或密码错误")

        if not security.verify_password(password, user.password):
            raise custom_exc.TokenAuthError(err_desc="账号或密码错误")

        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

        return security.create_access_token(user.id, expires_delta=access_token_expires)