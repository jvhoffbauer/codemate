    async def handle_http_request(self, http_request: Request):
        background_tasks = BackgroundTasks()

        sub_response = Response()
        del sub_response.headers["content-length"]
        sub_response.status_code = None  # type: ignore

        try:
            body = await self.parse_body(http_request)
        except Exception as exc:
            resp = await self.entrypoint.handle_exception_to_resp(exc)
            response = self.response_class(content=resp, background=background_tasks)
        else:
            try:
                resp = await self.handle_body(
                    http_request, background_tasks, sub_response, body
                )
            except NoContent:
                # no content for successful notifications
                response = Response(
                    media_type="application/json", background=background_tasks
                )
            else:
                response = self.response_class(
                    content=resp, background=background_tasks
                )

        response.headers.raw.extend(sub_response.headers.raw)
        if sub_response.status_code:
            response.status_code = sub_response.status_code

        return response