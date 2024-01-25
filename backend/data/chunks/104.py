def type_coerce(
    expression: Union[_ColumnExpressionOrLiteralArgument[Any], Any],
    type_: "_TypeEngineArgument[_T]",
) -> TypeCoerce[_T]:
    return sqlalchemy.type_coerce(expression, type_)  # type: ignore[arg-type]