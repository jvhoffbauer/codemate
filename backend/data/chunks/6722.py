    @cached_property
    def request(self) -> JsonRpcRequest:
        try:
            return self.request_class.model_validate(self.raw_request)
        except ValidationError as exc:
            raise invalid_request_from_validation_error(exc)