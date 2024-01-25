    def on_raw_response(
        self,
        raw_response: Union[dict, Exception],
    ):
        exception = None
        is_unhandled_exception = False

        if isinstance(raw_response, Exception):
            exception = raw_response
            if isinstance(exception, BaseError):
                raw_response = exception.get_resp()
            elif isinstance(exception, HTTPException):
                raw_response = None
            else:
                raw_response = InternalError().get_resp()
                is_unhandled_exception = True

        if raw_response is not None:
            raw_response.pop("id", None)
            if isinstance(self.raw_request, dict) and "id" in self.raw_request:
                raw_response["id"] = self.raw_request.get("id")
            elif "error" in raw_response:
                raw_response["id"] = None

        self._raw_response = raw_response
        self.exception = exception
        self.is_unhandled_exception = is_unhandled_exception