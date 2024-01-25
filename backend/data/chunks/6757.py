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
            dependency_cache = await self.solve_shared_dependencies(
                http_request,
                background_tasks,
                sub_response,
            )
        except BaseError as error:
            shared_dependencies_error = error
            dependency_cache = None

        scheduler = await self.entrypoint.get_scheduler()

        if isinstance(body, list):
            req_list = body
        else:
            req_list = [body]

        # Run concurrently through scheduler
        job_list = []
        for req in req_list:
            job = await scheduler.spawn(
                self.handle_req_to_resp(
                    http_request,
                    background_tasks,
                    sub_response,
                    req,
                    dependency_cache=dependency_cache,
                    shared_dependencies_error=shared_dependencies_error,
                )
            )
            job_list.append(job.wait())

        resp_list = []

        for resp in await asyncio.gather(*job_list):
            # No response for successful notifications
            has_content = "error" in resp or "id" in resp
            if not has_content:
                continue

            resp_list.append(resp)

        if not resp_list:
            raise NoContent

        if not isinstance(body, list):
            content = resp_list[0]
        else:
            content = resp_list

        return content