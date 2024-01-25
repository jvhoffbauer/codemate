def asc(
    column: Union[_ColumnExpressionOrStrLabelArgument[_T], _T],
) -> UnaryExpression[_T]:
    return sqlalchemy.asc(column)  # type: ignore[arg-type]