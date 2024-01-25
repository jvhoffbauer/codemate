def distinct(expr: Union[_ColumnExpressionArgument[_T], _T]) -> UnaryExpression[_T]:
    return sqlalchemy.distinct(expr)  # type: ignore[arg-type]