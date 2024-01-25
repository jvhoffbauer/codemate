    async def handle_body(
        self,
        http_request: Request,
        background_tasks: BackgroundTasks,
        sub_response: Response,
        body: Any,
    ) -> dict:
        # Shared dependencies for all requests in one json-rpc batch request
        shared_dependencies_error = None
        try:
            dependency_cache = await self.entrypoint.solve_shared_dependencies(
                http_request,
                background_tasks,
                sub_response,
            )
        except BaseError as error:
            shared_dependencies_error = error
            dependency_cache = None

        resp = await self.handle_req_to_resp(
            http_request,
            background_tasks,
            sub_response,
            body,
            dependency_cache=dependency_cache,
            shared_dependencies_error=shared_dependencies_error,
        )

        # No response for successful notifications
        has_content = "error" in resp or "id" in resp
        if not has_content:
            raise NoContent

        return resp