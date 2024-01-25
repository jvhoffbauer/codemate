def analyze_param(
    *,
    param_name: str,
    annotation: Any,
    value: Any,
    is_path_param: bool,
) -> Tuple[Any, Optional[params.Depends], Optional[ModelField]]:
    field_info = None
    depends = None
    type_annotation: Any = Any
    if (
        annotation is not inspect.Signature.empty
        and get_origin(annotation) is Annotated
    ):
        annotated_args = get_args(annotation)
        type_annotation = annotated_args[0]
        fastapi_annotations = [
            arg
            for arg in annotated_args[1:]
            if isinstance(arg, (FieldInfo, params.Depends))
        ]
        assert (
            len(fastapi_annotations) <= 1
        ), f"Cannot specify multiple `Annotated` FastAPI arguments for {param_name!r}"
        fastapi_annotation = next(iter(fastapi_annotations), None)
        if isinstance(fastapi_annotation, FieldInfo):
            # Copy `field_info` because we mutate `field_info.default` below.
            field_info = copy_field_info(
                field_info=fastapi_annotation, annotation=annotation
            )
            assert field_info.default is Undefined or field_info.default is Required, (
                f"`{field_info.__class__.__name__}` default value cannot be set in"
                f" `Annotated` for {param_name!r}. Set the default value with `=` instead."
            )
            if value is not inspect.Signature.empty:
                assert not is_path_param, "Path parameters cannot have default values"
                field_info.default = value
            else:
                field_info.default = Required
        elif isinstance(fastapi_annotation, params.Depends):
            depends = fastapi_annotation
    elif annotation is not inspect.Signature.empty:
        type_annotation = annotation

    if isinstance(value, params.Depends):
        assert depends is None, (
            "Cannot specify `Depends` in `Annotated` and default value"
            f" together for {param_name!r}"
        )
        assert field_info is None, (
            "Cannot specify a FastAPI annotation in `Annotated` and `Depends` as a"
            f" default value together for {param_name!r}"
        )
        depends = value
    elif isinstance(value, FieldInfo):
        assert field_info is None, (
            "Cannot specify FastAPI annotations in `Annotated` and default value"
            f" together for {param_name!r}"
        )
        field_info = value
        if PYDANTIC_V2:
            field_info.annotation = type_annotation

    if depends is not None and depends.dependency is None:
        depends.dependency = type_annotation

    if lenient_issubclass(
        type_annotation,
        (
            Request,
            WebSocket,
            HTTPConnection,
            Response,
            StarletteBackgroundTasks,
            SecurityScopes,
        ),
    ):
        assert depends is None, f"Cannot specify `Depends` for type {type_annotation!r}"
        assert (
            field_info is None
        ), f"Cannot specify FastAPI annotation for type {type_annotation!r}"
    elif field_info is None and depends is None:
        default_value = value if value is not inspect.Signature.empty else Required
        if is_path_param:
            # We might check here that `default_value is Required`, but the fact is that the same
            # parameter might sometimes be a path parameter and sometimes not. See
            # `tests/test_infer_param_optionality.py` for an example.
            field_info = params.Path(annotation=type_annotation)
        elif is_uploadfile_or_nonable_uploadfile_annotation(
            type_annotation
        ) or is_uploadfile_sequence_annotation(type_annotation):
            field_info = params.File(annotation=type_annotation, default=default_value)
        elif not field_annotation_is_scalar(annotation=type_annotation):
            field_info = params.Body(annotation=type_annotation, default=default_value)
        else:
            field_info = params.Query(annotation=type_annotation, default=default_value)

    field = None
    if field_info is not None:
        if is_path_param:
            assert isinstance(field_info, params.Path), (
                f"Cannot use `{field_info.__class__.__name__}` for path param"
                f" {param_name!r}"
            )
        elif (
            isinstance(field_info, params.Param)
            and getattr(field_info, "in_", None) is None
        ):
            field_info.in_ = params.ParamTypes.query
        use_annotation = get_annotation_from_field_info(
            type_annotation,
            field_info,
            param_name,
        )
        if not field_info.alias and getattr(field_info, "convert_underscores", None):
            alias = param_name.replace("_", "-")
        else:
            alias = field_info.alias or param_name
        field_info.alias = alias
        field = create_response_field(
            name=param_name,
            type_=use_annotation,
            default=field_info.default,
            alias=alias,
            required=field_info.default in (Required, Undefined),
            field_info=field_info,
        )

    return type_annotation, depends, field