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