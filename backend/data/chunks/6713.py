def make_request_model(name, module, body_params: List[ModelField]):
    whole_params_list = [p for p in body_params if isinstance(p.field_info, Params)]
    if len(whole_params_list):
        if len(whole_params_list) > 1:
            raise RuntimeError(
                f"Only one 'Params' allowed: " f"params={whole_params_list}"
            )
        body_params_list = [
            p for p in body_params if not isinstance(p.field_info, Params)
        ]
        if body_params_list:
            raise RuntimeError(
                f"No other params allowed when 'Params' used: "
                f"params={whole_params_list}, other={body_params_list}"
            )

    if whole_params_list:
        assert whole_params_list[0].alias == "params"
        params_field = whole_params_list[0]
        params_annotation, params_field_info = (
            params_field.field_info.annotation,
            params_field.field_info,
        )
    else:
        fields = {
            param.name: (param.field_info.annotation, param.field_info)
            for param in body_params
        }
        _JsonRpcRequestParams = create_model(
            f"_Params[{name}]",
            __base__=(BaseModel,),
            __module__=module,
            **fields,
        )
        _JsonRpcRequestParams = component_name(f"_Params[{name}]", module)(
            _JsonRpcRequestParams
        )

        params_annotation = _JsonRpcRequestParams
        params_field_info = ...

    _Request = create_model(
        f"_Request[{name}]",
        __config__=ConfigDict(extra="forbid"),
        __module__=module,
        jsonrpc=(Literal["2.0"], Field("2.0", json_schema_extra={"example": "2.0"})),
        id=(Union[StrictStr, int], Field(None, json_schema_extra={"example": 0})),
        method=(
            StrictStr,
            Field(name, frozen=True, json_schema_extra={"example": name}),
        ),
        params=(params_annotation, params_field_info),
    )
    _Request = component_name(f"_Request[{name}]", module)(_Request)

    return _Request