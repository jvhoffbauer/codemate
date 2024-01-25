def cast(
    expression: Union[_ColumnExpressionOrLiteralArgument[Any], Any],
    type_: "_TypeEngineArgument[_T]",
) -> Cast[_T]:
    return sqlalchemy.cast(expression, type_)  # type: ignore[arg-type]