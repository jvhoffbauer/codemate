def invalid_params_from_validation_error(
    exc: typing.Union[ValidationError, RequestValidationError]
) -> InvalidParams:
    errors = []

    for err in exc.errors():
        err.pop("url", None)

        if err["loc"][:1] == ("body",):
            err["loc"] = err["loc"][1:]
        else:
            assert err["loc"]
            err["loc"] = (f"<{err['loc'][0]}>",) + err["loc"][1:]
        errors.append(err)

    return InvalidParams(data={"errors": errors})