def try_cast(
    expression: Union[_ColumnExpressionOrLiteralArgument[Any], Any],
    type_: "_TypeEngineArgument[_T]",
) -> TryCast[_T]:
    return sqlalchemy.try_cast(expression, type_)  # type: ignore[arg-type]