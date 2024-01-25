def desc(
    column: Union[_ColumnExpressionOrStrLabelArgument[_T], _T],
) -> UnaryExpression[_T]:
    return sqlalchemy.desc(column)  # type: ignore[arg-type]