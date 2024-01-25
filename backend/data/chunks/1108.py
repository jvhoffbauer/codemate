def generate_operation_id(
    *, route: routing.APIRoute, method: str
) -> str:  # pragma: nocover
    warnings.warn(
        "fastapi.openapi.utils.generate_operation_id() was deprecated, "
        "it is not used internally, and will be removed soon",
        DeprecationWarning,
        stacklevel=2,
    )
    if route.operation_id:
        return route.operation_id
    path: str = route.path_format
    return generate_operation_id_for_path(name=route.name, path=path, method=method)