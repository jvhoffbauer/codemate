def nulls_first(
    column: Union[_ColumnExpressionArgument[_T], _T]
) -> UnaryExpression[_T]:
    return sqlalchemy.nulls_first(column)  # type: ignore[arg-type]