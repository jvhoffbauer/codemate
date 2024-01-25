def register_exception(app: FastAPI) -> None:
    """
    全局异常捕获
    注意 别手误多敲一个s
    exception_handler
    exception_handlers
    两者有区别
        如果只捕获一个异常 启动会报错
        @exception_handlers(UserNotFound)
    TypeError: 'dict' object is not callable
    :param app:
    :return:
    """

    # 自定义异常 捕获
    @app.exception_handler(custom_exc.TokenExpired)
    async def user_not_found_exception_handler(
        request: Request, exc: custom_exc.TokenExpired
    ):
        """
        token过期
        :param request:
        :param exc:
        :return:
        """
        logger.error(
            f"token未知用户\nURL:{request.method}{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}"
        )

        return resp.fail(message=exc.err_desc)

    @app.exception_handler(custom_exc.TokenAuthError)
    async def user_token_exception_handler(
        request: Request, exc: custom_exc.TokenAuthError
    ):
        """
        用户token异常
        :param request:
        :param exc:
        :return:
        """
        logger.error(
            f"用户认证异常\nURL:{request.method}{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}"
        )

        return resp.fail(resp.DataNotFound.set_msg(exc.err_desc))

    @app.exception_handler(custom_exc.AuthenticationError)
    async def user_not_found_exception_handler(
        request: Request, exc: custom_exc.AuthenticationError
    ):
        """
        用户权限不足
        :param request:
        :param exc:
        :return:
        """
        logger.error(f"用户权限不足 \nURL:{request.method}{request.url}")
        return resp.fail(resp.PermissionDenied)

    @app.exception_handler(ValidationError)
    async def inner_validation_exception_handler(
        request: Request, exc: ValidationError
    ):
        """
        内部参数验证异常
        :param request:
        :param exc:
        :return:
        """
        logger.error(
            f"内部参数验证错误\nURL:{request.method}{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}"
        )
        return resp.fail(resp.BusinessError.set_msg(exc.errors()))

    @app.exception_handler(RequestValidationError)
    async def request_validation_exception_handler(
        request: Request, exc: RequestValidationError
    ):
        """
        请求参数验证异常
        :param request:
        :param exc:
        :return:
        """
        logger.error(
            f"请求参数格式错误\nURL:{request.method}{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}"
        )
        # return response_code.resp_4001(message='; '.join([f"{e['loc'][1]}: {e['msg']}" for e in exc.errors()]))
        return resp.fail(resp.InvalidParams.set_msg(exc.errors()))

    # 捕获全部异常
    @app.exception_handler(Exception)
    async def all_exception_handler(request: Request, exc: Exception):
        """
        全局所有异常
        :param request:
        :param exc:
        :return:
        """
        logger.error(
            f"全局异常\n{request.method}URL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}"
        )
        return resp.fail(resp.ServerError)