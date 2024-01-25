def insfield_to_modelfield(insfield: InstrumentedAttribute) -> Optional[ModelField]:
    """InstrumentedAttribute to ModelField"""
    if not isinstance(insfield.property, ColumnProperty):
        return None
    expression = insfield.expression
    field_info_kwargs = {}
    required = not expression.nullable
    default = ...
    if expression.nullable:
        default = None
    if expression.default:
        if expression.default.is_scalar:
            default = expression.default.arg
            required = False
        elif expression.default.is_callable:
            field_info_kwargs["default_factory"] = expression.default.arg
            required = False
    if isinstance(expression.type, String):
        field_info_kwargs["max_length"] = expression.type.length
    if "default_factory" not in field_info_kwargs:
        field_info_kwargs["default"] = default
    type_ = expression.type.python_type
    if PYDANTIC_V2:
        field_info_kwargs["annotation"] = type_
    return create_response_field(
        name=insfield.key,
        type_=type_,
        required=required,
        field_info=Field(title=expression.comment, **field_info_kwargs),
    )