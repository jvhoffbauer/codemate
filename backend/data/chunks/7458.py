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