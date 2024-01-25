    async def handle_req(
        self,
        http_request: Request,
        background_tasks: BackgroundTasks,
        sub_response: Response,
        ctx: JsonRpcContext,
        dependency_cache: dict = None,
        shared_dependencies_error: BaseError = None,
    ):
        http_request_shadow = RequestShadow(http_request)
        http_request_shadow.scope["path"] = self.path + "/" + ctx.request.method

        for route in self.entrypoint.routes:  # type: MethodRoute
            match, child_scope = route.matches(http_request_shadow.scope)
            if match == Match.FULL:
                # http_request is a transport layer and it is common for all JSON-RPC requests in a batch
                ctx.method_route = route
                return await route.handle_req(
                    http_request_shadow,
                    background_tasks,
                    sub_response,
                    ctx,
                    dependency_cache=dependency_cache,
                    shared_dependencies_error=shared_dependencies_error,
                )
        else:
            raise MethodNotFound()