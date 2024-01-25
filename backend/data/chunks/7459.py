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