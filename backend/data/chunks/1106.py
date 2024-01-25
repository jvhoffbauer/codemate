def get_openapi_operation_parameters(
    *,
    all_route_params: Sequence[ModelField],
    schema_generator: GenerateJsonSchema,
    model_name_map: ModelNameMap,
    field_mapping: Dict[
        Tuple[ModelField, Literal["validation", "serialization"]], JsonSchemaValue
    ],
    separate_input_output_schemas: bool = True,
) -> List[Dict[str, Any]]:
    parameters = []
    for param in all_route_params:
        field_info = param.field_info
        field_info = cast(Param, field_info)
        if not field_info.include_in_schema:
            continue
        param_schema = get_schema_from_model_field(
            field=param,
            schema_generator=schema_generator,
            model_name_map=model_name_map,
            field_mapping=field_mapping,
            separate_input_output_schemas=separate_input_output_schemas,
        )
        parameter = {
            "name": param.alias,
            "in": field_info.in_.value,
            "required": param.required,
            "schema": param_schema,
        }
        if field_info.description:
            parameter["description"] = field_info.description
        if field_info.openapi_examples:
            parameter["examples"] = jsonable_encoder(field_info.openapi_examples)
        elif field_info.example != Undefined:
            parameter["example"] = jsonable_encoder(field_info.example)
        if field_info.deprecated:
            parameter["deprecated"] = field_info.deprecated
        parameters.append(parameter)
    return parameters