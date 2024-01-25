    async def handle(
        self, request: Request, data: BaseModel, **kwargs
    ) -> BaseApiOut[Any]:
        if data.username == "amisadmin" and data.password == "amisadmin":
            return BaseApiOut(msg="登录成功!", data={"token": "xxxxxx"})
        return BaseApiOut(status=-1, msg="用户名或密码错误!")