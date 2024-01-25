def errors_responses(errors: Sequence[Type[BaseError]] = None):
    responses = {"default": {}}

    if errors:
        # Swagger UI 5.0 and above allow use only int status_codes and in _valid range_
        # generate fake status codes for each error
        for fake_status_code, error_cls in enumerate(errors, start=210):
            responses[fake_status_code] = {
                "model": error_cls.get_resp_model(),
                "description": error_cls.get_description(),
            }

    return responses