    async def ep_middleware(ctx: JsonRpcContext):
        credentials = await security(ctx.http_request)
        credentials = auth_user(credentials)
        credentials_var_token = credentials_var.set(credentials)

        try:
            yield
        finally:
            credentials_var.reset(credentials_var_token)