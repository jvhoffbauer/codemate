def bitwise_not(expr: Union[_ColumnExpressionArgument[_T], _T]) -> UnaryExpression[_T]:
    return sqlalchemy.bitwise_not(expr)  # type: ignore[arg-type]