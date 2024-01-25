async def request_body_to_args(
    required_params: List[ModelField],
    received_body: Optional[Union[Dict[str, Any], FormData]],
) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    values = {}
    errors: List[Dict[str, Any]] = []
    if required_params:
        field = required_params[0]
        field_info = field.field_info
        embed = getattr(field_info, "embed", None)
        field_alias_omitted = len(required_params) == 1 and not embed
        if field_alias_omitted:
            received_body = {field.alias: received_body}

        for field in required_params:
            loc: Tuple[str, ...]
            if field_alias_omitted:
                loc = ("body",)
            else:
                loc = ("body", field.alias)

            value: Optional[Any] = None
            if received_body is not None:
                if (is_sequence_field(field)) and isinstance(received_body, FormData):
                    value = received_body.getlist(field.alias)
                else:
                    try:
                        value = received_body.get(field.alias)
                    except AttributeError:
                        errors.append(get_missing_field_error(loc))
                        continue
            if (
                value is None
                or (isinstance(field_info, params.Form) and value == "")
                or (
                    isinstance(field_info, params.Form)
                    and is_sequence_field(field)
                    and len(value) == 0
                )
            ):
                if field.required:
                    errors.append(get_missing_field_error(loc))
                else:
                    values[field.name] = deepcopy(field.default)
                continue
            if (
                isinstance(field_info, params.File)
                and is_bytes_field(field)
                and isinstance(value, UploadFile)
            ):
                value = await value.read()
            elif (
                is_bytes_sequence_field(field)
                and isinstance(field_info, params.File)
                and value_is_sequence(value)
            ):
                # For types
                assert isinstance(value, sequence_types)  # type: ignore[arg-type]
                results: List[Union[bytes, str]] = []

                async def process_fn(
                    fn: Callable[[], Coroutine[Any, Any, Any]]
                ) -> None:
                    result = await fn()
                    results.append(result)  # noqa: B023

                async with anyio.create_task_group() as tg:
                    for sub_value in value:
                        tg.start_soon(process_fn, sub_value.read)
                value = serialize_sequence_value(field=field, value=results)

            v_, errors_ = field.validate(value, values, loc=loc)

            if isinstance(errors_, list):
                errors.extend(errors_)
            elif errors_:
                errors.append(errors_)
            else:
                values[field.name] = v_
    return values, errors