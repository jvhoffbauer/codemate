def is_body_param(*, param_field: ModelField, is_path_param: bool) -> bool:
    if is_path_param:
        assert is_scalar_field(
            field=param_field
        ), "Path params must be of one of the supported types"
        return False
    elif is_scalar_field(field=param_field):
        return False
    elif isinstance(
        param_field.field_info, (params.Query, params.Header)
    ) and is_scalar_sequence_field(param_field):
        return False
    else:
        assert isinstance(
            param_field.field_info, params.Body
        ), f"Param: {param_field.name} can only be a request body, using Body()"
        return True